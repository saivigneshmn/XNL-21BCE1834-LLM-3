import shap
import joblib
import numpy as np

if __name__ == "__main__":
    model = joblib.load("models/fraud_detection_model.pkl")
    X_test = np.load("data/combined_features.npy")  # Use test data
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    shap.summary_plot(shap_values, X_test)