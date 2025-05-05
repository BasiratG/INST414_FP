import pandas as pd
import statsmodels.api as sm

# Data Validation
print("Initial Data Overview:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())


# Handle missing values (if applicable)
df = df.dropna()


# Remove duplicates
df = df.drop_duplicates()


# Check for 'Gender' column existence before encoding
if 'Gender' in df.columns:
   le = LabelEncoder()
   df['Gender'] = le.fit_transform(df['Gender'])
else:
   print("'Gender' column not found in the dataset.")


# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())


# Exploratory Data Analysis
# Histogram of Stress Scores
plt.figure(figsize=(8,5))
sns.histplot(df['Survey_Stress_Score'], kde=True)
plt.title('Distribution of Survey Stress Scores')
plt.show()


# Box Plot of Social Media Hours by Gender
if 'Gender' in df.columns:
   plt.figure(figsize=(8,5))
   sns.boxplot(x='Gender', y='Social_Media_Hours', data=df)
   plt.title('Social Media Hours by Gender')
   plt.show()
else:
   print("'Gender' column not available for Box Plot.")


# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])


# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()




# Correlation Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()




# Scatter Plot: Social Media Hours vs Stress Scores
plt.figure(figsize=(8,5))
sns.scatterplot(x='Social_Media_Hours', y='Survey_Stress_Score', data=df)
plt.title('Social Media Hours vs. Stress Score')
plt.show()


# Hypothesis Testing
# Hypothesis 1: Social Media Hours and Stress Levels
if 'Social_Media_Hours' in df.columns and 'Survey_Stress_Score' in df.columns:
   correlation, p_value = pearsonr(df['Social_Media_Hours'], df['Survey_Stress_Score'])
   print(f"Pearson Correlation: {correlation}, P-Value: {p_value}")
else:
   print("Columns for hypothesis testing not found.")


# Hypothesis 2: Academic Performance and Gender
if 'Gender' in df.columns and 'Academic_Performance' in df.columns:
   contingency_table = pd.crosstab(df['Gender'], df['Academic_Performance'])
   chi2, p, F_, _ = chi2_contingency(contingency_table)
   print(f"Chi-Square Test: Chi2={chi2}, P-Value={p}")
else:
   print("Columns for Chi-Square test not found.")


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
    
    # Convert categorical variable 'Gender' and 'Academic_Performance' into dummy variables
    df_encoded = pd.get_dummies(df, columns=['Gender', 'Academic_Performance'], drop_first=True)
    
    # Define predictors (X) and outcome (y)
    X = df_encoded[['Social_Media_Hours'] + 
                   [col for col in df_encoded.columns if col.startswith('Gender_') or col.startswith('Academic_Performance_')]]
    y = df_encoded['Survey_Stress_Score']
    
    # Add constant to model (for intercept)
    X = sm.add_constant(X)
    
    # Fit model
    model = sm.OLS(y, X).fit()
    
    return model.summary(), model

# Load the dataset
df = pd.read_csv("/Users/basiratgbadegesin/Documents/INST414_FP-2/mental_health_analysis.csv")

# Run the regression
summary, model = run_regression(df)

# Print the regression summary
print(summary)
