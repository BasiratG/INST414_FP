import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column, title):
    """
    Plots a histogram with a KDE for the specified column in the DataFrame.

    Parameters:
    df (DataFrame): The dataset
    column (str): The column name to plot
    title (str): The title of the plot
    """
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.show()

def plot_boxplot(df, x_column, y_column, title):
    """
    Plots a boxplot to show distribution of a numerical variable across categories.

    Parameters:
    df (DataFrame): The dataset
    x_column (str): The categorical column
    y_column (str): The numerical column
    title (str): The title of the plot
    """
    plt.figure(figsize=(8,5))
    sns.boxplot(x=x_column, y=y_column, data=df)
    plt.title(title)
    plt.show()

def plot_scatter(df, x_column, y_column, title):
    """
    Plots a scatter plot to visualize the relationship between two numerical variables.

    Parameters:
    df (DataFrame): The dataset
    x_column (str): The x-axis column
    y_column (str): The y-axis column
    title (str): The title of the plot
    """
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=x_column, y=y_column, data=df)
    plt.title(title)
    plt.show()

def plot_heatmap(df, columns, title):
    """
    Plots a heatmap to visualize the correlation between specified columns.

    Parameters:
    df (DataFrame): The dataset
    columns (list): List of column names to compute correlations
    title (str): The title of the plot
    """
    correlation_matrix = df[columns].corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title(title)
    plt.show()
