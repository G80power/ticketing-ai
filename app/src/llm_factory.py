"""use this llm_factory_api.py if you are using hugging face inference"""

import os
import requests

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Load model directly

class LLMFactory:
    def __init__(self):
        self.hf_api_token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.hf_headers = {"Authorization": f"Bearer {self.hf_api_token}"}
        self.hf_classification_model_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
        # You can add more model URLs or API keys here for other models
    
    def classify_ticket(self, text: str):
        payload = {"inputs": text}
        response = requests.post(self.hf_classification_model_url, headers=self.hf_headers, json=payload)
        response.raise_for_status()
        return response.json()

    # Add more methods for other models or tasks as needed


# Usage example:
# llm = LLMFactory()
# result = llm.classify_ticket("My internet is down.")
# print(result)
