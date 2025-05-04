import pandas as pd
import statsmodels.api as sm

def run_regression(df):
    """
    Runs a multiple linear regression predicting stress from 
    social media hours, gender, and academic performance.

    Parameters:
    df (DataFrame): Cleaned dataset with appropriate columns.

    Returns:
    summary: Regression summary
    model: Trained regression model
    """
    # Check required columns
    required_cols = ['Survey_Stress_Score', 'Social_Media_Hours', 'Gender', 'Academic_Performance']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Missing required columns. Expected: {required_cols}")
    
    # Convert categorical variable 'Academic_Performance' into dummy variables
    df_encoded = pd.get_dummies(df, columns=['Academic_Performance'], drop_first=True)

    # Define predictors (X) and outcome (y)
    X = df_encoded[['Social_Media_Hours', 'Gender'] + 
                   [col for col in df_encoded.columns if col.startswith('Academic_Performance_')]]
    y = df_encoded['Survey_Stress_Score']
    
    # Add constant to model (for intercept)
    X = sm.add_constant(X)

    # Fit model
    model = sm.OLS(y, X).fit()

    return model.summary(), model
