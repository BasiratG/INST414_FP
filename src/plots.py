import matplotlib.pyplot as plt
import seaborn as sns

def plot_stress_distribution(df):
    """
    Plots the distribution of survey stress scores.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Survey_Stress_Score'], kde=True)
    plt.title('Distribution of Survey Stress Scores')
    plt.xlabel('Stress Score')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()


def plot_social_media_vs_stress(df):
    """
    Scatter plot: Social media hours vs stress score.
    """
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Social_Media_Hours', y='Survey_Stress_Score', data=df)
    plt.title('Social Media Hours vs. Stress Score')
    plt.xlabel('Social Media Hours')
    plt.ylabel('Stress Score')
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    """
    Plots a correlation heatmap of numeric variables.
    """
    plt.figure(figsize=(10, 8))

