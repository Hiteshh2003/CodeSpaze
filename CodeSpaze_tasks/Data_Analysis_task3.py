import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def load_dataset():
    """
    Load the Iris dataset from an online source.
    """
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    data = pd.read_csv(url)
    print("Dataset loaded successfully!")
    return data

def basic_analysis(data):
    """
    Perform basic analysis of the dataset.
    """
    print("\n--- Dataset Head ---")
    print(data.head())
    print("\n--- Dataset Info ---")
    print(data.info())
    print("\n--- Summary Statistics ---")
    print(data.describe())

def static_visualizations(data):
    """
    Create static visualizations using Seaborn and Matplotlib.
    """
    # Pairplot for relationships
    sns.pairplot(data, hue="species", diag_kind="kde")
    plt.title("Pairplot of Iris Dataset")
    plt.show()

    # Boxplot for feature distribution
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="species", y="sepal_length", data=data)
    plt.title("Sepal Length Distribution by Species")
    plt.show()

def interactive_visualizations(data):
    """
    Create interactive visualizations using Plotly.
    """
    # Scatter plot
    fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species",
                     title="Sepal Width vs Sepal Length by Species",
                     labels={"sepal_width": "Sepal Width", "sepal_length": "Sepal Length"})
    fig.show()

    # Histogram
    fig = px.histogram(data, x="petal_length", color="species", nbins=20,
                       title="Petal Length Distribution by Species",
                       labels={"petal_length": "Petal Length"})
    fig.show()

if __name__ == "__main__":
    # Step 1: Load the dataset
    iris_data = load_dataset()
    
    # Step 2: Perform basic analysis
    basic_analysis(iris_data)
    
    # Step 3: Create static visualizations
    print("\nGenerating static visualizations...")
    static_visualizations(iris_data)
    
    # Step 4: Create interactive visualizations
    print("\nGenerating interactive visualizations...")
    interactive_visualizations(iris_data)
