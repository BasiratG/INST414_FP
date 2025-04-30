# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, chi2_contingency
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'mental_health_analysis.csv'
df = pd.read_csv(file_path)

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
    chi2, p, _, _ = chi2_contingency(contingency_table)
    print(f"Chi-Square Test: Chi2={chi2}, P-Value={p}")
else:
    print("Columns for Chi-Square test not found.")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('adolescent_mental_health.csv')  # <-- adjust filename

# Select features and target
X = data[['Social_Media_Hours', 'Sleep_Hours', 'Exercise_Hours']]
y = data['Stress_Score']

# Split into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)
