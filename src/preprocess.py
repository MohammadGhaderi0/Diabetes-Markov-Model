import pandas as pd
import numpy as np

def load_and_clean_data(file_path="data/diabetes.csv"):
    """
    Load and clean Kaggle diabetes dataset.
    :param file_path: Path to diabetes.csv
    :return: Cleaned DataFrame
    """
    df = pd.read_csv(file_path)
    # Replace invalid zeros with NaN for Glucose, Insulin, BMI, BloodPressure, SkinThickness
    for col in ["Glucose", "Insulin", "BMI", "BloodPressure", "SkinThickness"]:
        df[col] = df[col].replace(0, np.nan)
    # Drop rows with NaN (or impute if preferred)
    df = df.dropna()
    return df

def define_states(df):
    """
    Define diabetes states based on Glucose levels.
    :param df: Cleaned DataFrame
    :return: DataFrame with 'State' column
    """
    # Define states based on Glucose (inspired by WHO criteria and clinical guidelines)
    conditions = [
        (df["Glucose"] < 140),              # Controlled (normal or well-managed)
        (df["Glucose"] >= 140) & (df["Glucose"] < 200),  # Uncontrolled (pre-diabetes or poorly managed)
        (df["Glucose"] >= 200)              # Severe (likely complications)
    ]
    state_names = ["Controlled", "Uncontrolled", "Severe"]
    df["State"] = np.select(conditions, state_names, default="Unknown")
    return df

def estimate_state_distribution(df):
    """
    Calculate initial state distribution.
    :param df: DataFrame with 'State' column
    :return: Dictionary of state proportions
    """
    state_counts = df["State"].value_counts(normalize=True)
    return state_counts.to_dict()

if __name__ == "__main__":
    # Example usage
    df = load_and_clean_data()
    df = define_states(df)
    print("Cleaned DataFrame:\n", df.head())
    print("State Distribution:\n", estimate_state_distribution(df))