import pandas as pd

def load_data(file_path):
    """
    Loads the dataset from a CSV file.

    Parameters:
    file_path (str): Path to the dataset file.

    Returns:
    df (DataFrame): Loaded dataset.
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Cleans the dataset by handling missing values, duplicates, and irrelevant columns.

    Parameters:
    df (DataFrame): Raw dataset.

    Returns:
    df (DataFrame): Cleaned dataset.
    """
    # Drop rows with missing values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    # You can add more data cleaning steps as needed
    return df


def preprocess_data(df):
    """
    Preprocesses the dataset for analysis (e.g., encoding categorical variables).

    Parameters:
    df (DataFrame): Cleaned dataset.

    Returns:
    df (DataFrame): Preprocessed dataset.
    """
    # Example: Encoding the 'Gender' column (if it exists)
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
    
    # You can add more preprocessing steps as needed
    return df


def load_and_preprocess_data(file_path):
    """
    Loads, cleans, and preprocesses the dataset.

    Parameters:
    file_path (str): Path to the dataset file.

    Returns:
    df (DataFrame): Cleaned and preprocessed dataset.
    """
    df = load_data(file_path)
    df = clean_data(df)
    df = preprocess_data(df)
    return df
