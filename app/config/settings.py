import logging
from typing import Literal
from pydantic import BaseModel,Field


def setup_logging():
    """Configure basic logging for the application."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

class Reply(BaseModel):
    label: Literal['general', 'tech', 'product', 'other'] = Field(description="Category of the ticket")
    score: float = Field(description="Confidence score of the classification")


LABEL_MAP = {
    "POSITIVE": "general",
    "NEGATIVE": "tech",
    # Add more mappings as necessary
}