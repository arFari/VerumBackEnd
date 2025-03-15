from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import traceback
from openai import OpenAI
import json
app = Flask(__name__)

# Load the local model
MODEL_PATH = "BiasDetectorModel"  # Ensure this is the correct folder name
try:
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    print("Tokenizer loaded.")

    print("Loading model...")
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)
    print("Model loaded.")
except Exception as e:
    print("Failed to load model or tokenizer:")
    traceback.print_exc()
    raise e  # Stop execution if the model fails to load
GPT_TOKEN = "INSERT TOKEN HERE"
# Initialize OpenAI Client
client = OpenAI(api_key=GPT_TOKEN)  # Ensure your .env file is set correctly


def gpt_bias(prompt):
    """Send text to OpenAI GPT-4 and return bias classification with explanations."""
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI trained to output results in a structured JSON format. "
                        "For each article, classify it as 'Bias' or 'Unbiased' and provide 1-3 explanations. "
                        "Ensure the output is in JSON format with the following structure: "
                        '{"bias": <0 or 1>, "reasons": [{"reason": "reason1", "description": "desc1", "sentence": "sentence1"}, ...]} '
                        "where 'bias' is 1 for 'Unbiased' and 0 for 'Bias'. "
                        "Explain why the article is biased (if any), and also map each reason to a specific sentence in the article."
                    )
                },
                {
                    "role": "user",
                    "content": prompt  # The article or prompt content goes here
                }
            ]
        )

        bias_analysis = json.loads(response.choices[0].message.content)  # Fix here

        return bias_analysis  # Now returns a Python dict instead of a string

    except Exception as e:
        print("ERROR in GPT bias analysis:")
        traceback.print_exc()
        return {"error": str(e)}  # Return error details if the GPT call fails


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Retrieve text from form data
        text = request.form.get("text")
        print(f"Received text: {text}")  # Debug print

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Tokenize the input text
        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        # Run inference using the local model
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits

        # Convert logits to predicted label (0 or 1)
        predicted_label = torch.argmax(logits, dim=1).item()

        # Get bias analysis from GPT-4
        bias_analysis = gpt_bias(text)

        # Return both local model prediction and GPT-4 bias analysis
        return ({
            "local_model_prediction": predicted_label,
            "gpt_bias_analysis": bias_analysis
        }), 200

    except Exception as e:
        print("ERROR TRACEBACK:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)

