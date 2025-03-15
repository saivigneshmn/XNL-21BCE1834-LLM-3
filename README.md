# Fraud Detection System

## Overview
This project is a fraud detection system that leverages LLM embeddings and transformer models to analyze transaction descriptions, detect anomalies, and flag potential fraudulent activities. The system integrates with a vector database for rapid similarity search and provides real-time alerts.

## Architecture

![image](https://github.com/user-attachments/assets/d0c8d628-77d0-485d-8454-56b7d72201bd)

## Workflow

![image](https://github.com/user-attachments/assets/f7ab76bd-89c1-49e8-978c-702b5982fbc2)

## Features
- **Data Generation**: Simulates a massive transaction dataset.
- **Feature Engineering**: Extracts multi-modal features (text, numerical, embeddings).
- **Embedding Generation**: Uses FinBERT to generate transaction embeddings.
- **Fraud Detection Model**: Trains a hybrid model (LLM + traditional ML).
- **Vector Database**: Implements FAISS for similarity search.
- **Real-Time Processing**: Uses Kafka and PySpark for distributed processing.
- **Explainable AI**: Provides SHAP explanations for model predictions.
- **Alert System**: Sends real-time SMS alerts for fraudulent transactions.

## Docker 
![Screenshot (816)](https://github.com/user-attachments/assets/c60189fb-2ddd-4a32-a147-14ad11f3e7ca)

## Working

![image](https://github.com/user-attachments/assets/cab7c37a-4a1a-4fea-bc93-e040db06e8f9)

![image](https://github.com/user-attachments/assets/0a086345-a932-47f1-aa98-107c33c8bf67)

![WhatsApp Image 2025-03-15 at 08 50 24_70fac534](https://github.com/user-attachments/assets/06bbfcb8-2677-4de8-b1a3-3e25fb2c6c4c)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saivigneshmn/XNL-21BCE1834-LLM-3.git

## Install dependencies:
pip install -r requirements.txt

## Build the Docker image:
docker build -t fraud-detection-pipeline .

## Run the container:
docker run --rm fraud-detection-pipeline

## Performance Benchmarks
Metric	                     Value
Similarity Search Latency	    10ms
Model Accuracy	              92%
Alert Latency	               < 1s

## Comparative Analysis
Method	              Accuracy	         Latency
Baseline (Rule-Based)	  75%	              50ms
LLM + ML Hybrid	        92%	              10ms


## Demo Video
Watch the Demo Video
