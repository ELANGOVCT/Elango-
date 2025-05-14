import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model(input_path, model_path):
    df = pd.read_csv(input_path)
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    joblib.dump(clf, model_path)
    print("Model trained and saved to", model_path)

if __name__ == "__main__":
    train_model("../data/sample_input.csv", "model.pkl")
