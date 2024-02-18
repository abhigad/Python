import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Generate some random data
np.random.seed(0)
X = np.random.rand(10, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1)

print(X)

print("===================")

print(y)

print("===================")

# Split the data into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

print(X_train)

print("===================")

print(X_test)

print("===================")

print(y_train)

print("===================")

print(y_test)

print("===================")

# Train a simple linear regression model
model = LinearRegression()

model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert the regression problem into a binary classification problem
# We'll classify values as '1' if they are above a threshold, and '0' otherwise.
threshold = 6.0
y_pred_class = np.where(y_pred > threshold, 1, 0)
y_test_class = np.where(y_test > threshold, 1, 0)

# Calculate accuracy, precision, recall, and F1 score
accuracy = accuracy_score(y_test_class, y_pred_class)
precision = precision_score(y_test_class, y_pred_class)
recall = recall_score(y_test_class, y_pred_class)
f1 = f1_score(y_test_class, y_pred_class)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Generate a confusion matrix
cm = confusion_matrix(y_test_class, y_pred_class)

# Visualize the confusion matrix
plt.figure(figsize=(5, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
