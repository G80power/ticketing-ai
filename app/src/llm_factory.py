import os
import requests
import torch
from transformers import pipeline


class LLMFactory:
    def __init__(self):
        device = 0 if torch.cuda.is_available() else -1  # GPU or CPU device id for pipeline
        self.model = pipeline(
            "text-classification",
            model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
            device=device
        )

    def classify_ticket(self, text: str) -> Reply:
        result = self.model(text)[0]
        mapped_label = LABEL_MAP.get(result['label'], 'other')  # default to 'other'
        return Reply(label=mapped_label, score=result['score'])