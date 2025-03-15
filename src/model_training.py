from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import joblib

if __name__ == "__main__":
    combined_features = np.load("data/combined_features.npy")
    merchant_embeddings = np.load("data/merchant_embeddings.npy")
    transaction_data = pd.read_csv("data/transaction_data.csv")
    
    X = np.hstack((combined_features, merchant_embeddings))
    y = transaction_data["label"].apply(lambda x: 1 if x == "fraudulent" else 0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    joblib.dump(model, "models/fraud_detection_model.pkl")
    print(f"Model Accuracy: {model.score(X_test, y_test)}")