# Use an official Python runtime as the base image
FROM python:3.9-slim

# Install Java (required for PySpark)
RUN apt-get update && apt-get install -y openjdk-17-jre-headless && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Command to run the pipeline
CMD ["python", "src/pipeline.py"]