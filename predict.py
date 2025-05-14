import pandas as pd
import joblib
import sys

def predict_quality(input_path, model_path):
    df = pd.read_csv(input_path)
    model = joblib.load(model_path)
    predictions = model.predict(df)
    print("Predictions:", predictions)

if __name__ == "__main__":
    predict_quality("../data/sample_input.csv", "model.pkl")
