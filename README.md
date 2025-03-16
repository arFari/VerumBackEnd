# Verum Backend API Documentation

Welcome to the **Verum Backend API** documentation. This guide details the API and model used for analyzing bias in news articles. The backend leverages two advanced AI models—**roBERTa-base** for classification and **GPT-4 Turbo** for detailed analysis—to determine whether an article is biased or unbiased, along with providing key insights, highlighted biased text segments, and explanations.

---

## Overview

The Verum Backend API performs bias detection by combining two complementary approaches:

- **roBERTa-based Analysis**:  
  A fine-tuned version of the [roBERTa-base](https://huggingface.co/FacebookAI/roberta-base) model is used to classify text as biased or unbiased.

- **GPT-4 Turbo Analysis**:  
  The GPT-4 Turbo API is leveraged to deliver:
  - A binary bias indicator.
  - **Keypoints**: Extracted insights from the text.
  - **Biased Text Segments**: Specific parts of the text identified as biased.
  - **Reason**: A detailed explanation for the bias assessment.

This dual-model approach ensures a comprehensive evaluation of news articles for bias.

---

## Features

- **Dual Analysis System**:  
  Combines predictions from both a fine-tuned roBERTa model and GPT-4 Turbo for robust bias detection.

- **Detailed Reporting**:  
  Returns binary bias indicators along with keypoints, biased text segments, and a thorough explanation of the analysis.

- **FastAPI Powered**:  
  Built with FastAPI for rapid and asynchronous API responses.

- **Seamless Integration**:  
  Designed as a RESTful API that can be easily integrated with your frontend extensions or other applications.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- An OpenAI API key with access to GPT-4 Turbo

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/verum-backend-api.git
    cd verum-backend-api
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv env
    ```

3. **Activate the Virtual Environment**

    - On macOS/Linux:
      ```bash
      source env/bin/activate
      ```
    - On Windows:
      ```bash
      env\Scripts\activate
      ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure API Keys**

   Set your OpenAI API key in your environment. For example, create a `.env` file or export the key directly:

    ```bash
    export OPENAI_API_KEY="your-openai-api-key"
    ```

---

## Usage

### Running the API Server

Start the FastAPI server by executing:

```bash
python main.py
