import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads the mental health dataset and performs basic cleaning:
    - Drops missing values
    - Removes duplicates
    - Encodes gender as binary (0 = Male, 1 = Female)

    Parameters:
    filepath (str): Path to the CSV file

    Returns:
    DataFrame: Cleaned pandas DataFrame
    """
    df = pd.read_csv(filepath)

    # Drop missing values
    df = df.dropna()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Encode Gender if it's still a string
    if df['Gender'].dtype == 'object':
        df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    return df

