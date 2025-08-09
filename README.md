# AI Ticket Prioritization & Routing System

## Overview  
This project builds an AI-powered system that analyzes customer support tickets, classifies their topic and priority, and routes them to the appropriate department automatically using OpenAI's GPT models.

## Problem Statement  
Customer support teams receive a large volume of tickets daily. Manually sorting and prioritizing them is slow and error-prone. Automating this process improves response times and customer satisfaction.

## Inputs and Outputs  
- **Input:** Text of customer support tickets  
- **Output:** Ticket category (e.g., Technical Support, Billing), priority level (High, Medium, Low), and routing assignment.

## Key Components  
- Ticket ingestion and preprocessing  
- LLM API call for classification and priority  
- Routing logic to assign tickets to departments  
- Logging and error handling

## Flow Summary  
1. Receive ticket text  
2. Send ticket to LLM with prompt for classification and priority  
3. Parse LLM response  
4. Route ticket based on classification

## Tech Stack  
- Python 3.10+  
- OpenAI API  
- Requests library  
- dotenv for managing API keys

