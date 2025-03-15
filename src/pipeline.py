import subprocess

# Run all steps in sequence
subprocess.run(["python", "src/data_generation.py"])
subprocess.run(["python", "src/feature_engineering.py"])
subprocess.run(["python", "src/embedding_generation.py"])
subprocess.run(["python", "src/model_training.py"])
subprocess.run(["python", "src/vector_database.py"])
subprocess.run(["python", "src/realtime_processing.py"])
subprocess.run(["python", "src/explainable_ai.py"])
subprocess.run(["python", "src/alert_system.py"])