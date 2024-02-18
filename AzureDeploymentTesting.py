# Example: Save a scikit-learn model to a file
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Train the model (replace with your actual training process)
model = RandomForestClassifier()

# Generate synthetic data using scikit-learn's make_classification
X, y = make_classification(n_samples=1000, n_features=10, n_informative=8, n_redundant=2, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Assuming you have X_train, y_train
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'model.pkl')
