from openai import OpenAI

client = OpenAI(
  api_key="../.env/OPENAI_KEY"
)


def gpt_bias(prompt):

    # First request: Get bias classification and explanations
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


    bias_analysis = response.choices[0].message.content
    print("Bias Analysis Output:")
    print(bias_analysis)  # First output (Bias + Explanations)


