import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from joblib import dump, load
import os

# Step 1: Load Data
def load_data():
    """
    Load the Iris dataset.
    """
    from sklearn.datasets import load_iris
    data = load_iris(as_frame=True)
    df = data['frame']
    X = df.drop(columns=['target'])
    y = df['target']
    return X, y

# Step 2: Build the Pipeline
def create_pipeline():
    """
    Create a machine learning pipeline with preprocessing and model training.
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', LogisticRegression(random_state=42))
    ])
    return pipeline

# Step 3: Train the Model
def train_model(pipeline, X_train, y_train):
    """
    Train the machine learning model.
    """
    pipeline.fit(X_train, y_train)
    return pipeline

# Step 4: Evaluate the Model
def evaluate_model(pipeline, X_test, y_test):
    """
    Evaluate the model and print metrics.
    """
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# Step 5: Save the Model
def save_model(pipeline, filename="model.joblib"):
    """
    Save the trained model to a file.
    """
    dump(pipeline, filename)
    print(f"Model saved to {filename}")

# Step 6: Load the Model (Optional)
def load_model(filename="model.joblib"):
    """
    Load the trained model from a file.
    """
    if os.path.exists(filename):
        return load(filename)
    else:
        print(f"Model file {filename} not found!")
        return None

# Main Workflow
if __name__ == "__main__":
    # Load the data
    X, y = load_data()

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create the pipeline
    pipeline = create_pipeline()

    # Train the model
    pipeline = train_model(pipeline, X_train, y_train)

    # Evaluate the model
    evaluate_model(pipeline, X_test, y_test)

    # Save the model
    save_model(pipeline)

    # Optional: Reload the model and predict
    reloaded_model = load_model()
    if reloaded_model:
        sample = X_test.iloc[:1]  # Take a sample from the test data
        print("Sample Prediction:", reloaded_model.predict(sample))
