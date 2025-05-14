import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    # Add additional preprocessing steps here
    return df

if __name__ == "__main__":
    sample_path = "../data/sample_input.csv"
    data = load_and_clean_data(sample_path)
    print(data.head())
