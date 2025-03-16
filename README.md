# Verum Backend API Documentation

Welcome to the **Verum Backend API** documentation. This guide details the Flask-based API and model used for analyzing bias in news articles. The backend integrates two powerful AI models—**roBERTa-base** for classification and **GPT-4 Turbo** for detailed analysis—to determine whether an article is biased or unbiased, along with providing key insights, highlighted biased text segments, and explanations.

---

## Overview

The Verum Backend API performs bias detection using a dual-model approach:

- **roBERTa-based Analysis**  
  A fine-tuned version of the [roBERTa-base](https://huggingface.co/FacebookAI/roberta-base) model is used to classify text as biased or unbiased.

- **GPT-4 Turbo Analysis**  
  The API leverages the GPT-4 Turbo API to provide:
  - A binary bias indicator.
  - **Keypoints**: Extracted insights from the text.
  - **Biased Text Segments**: Specific parts of the text identified as biased.
  - **Reason**: A detailed explanation for the bias determination.

This combination ensures a comprehensive and accurate analysis of news articles for bias.

---

## Features

- **Dual Analysis System**:  
  Combines predictions from both a fine-tuned roBERTa model and GPT-4 Turbo for robust bias detection.

- **Detailed Reporting**:  
  Returns binary bias indicators along with keypoints, biased text segments, and a thorough explanation of the analysis.

- **Flask-Powered API**:  
  The API is built with Flask, making it lightweight and easy to deploy.

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

    Set your OpenAI API key in app.py

    ```bash
    GPT_TOKEN = "INSERT GPT TOKEN HERE"
    ```

---

## Usage

### Running the API Server

The Flask server is started from the `app.py` file. To run the server, execute:

```bash
python app.py
