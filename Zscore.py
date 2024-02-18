import numpy as np
import matplotlib.pyplot as plt


def z_score(data):
    """
    Calculate Z-Scores for a given dataset.

    Parameters:
    - data: NumPy array or list

    Returns:
    - z_scores: NumPy array of Z-Scores
    """
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = (data - mean) / std_dev
    return z_scores

# Example dataset
data = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

# Calculate Z-Scores
z_scores_result = z_score(data)

# Display the original data and corresponding Z-Scores
for i in range(len(data)):
    print(f"Data Point: {data[i]}, Z-Score: {z_scores_result[i]}")

plt.figure(figsize=(10, 6))

# Original Data
plt.scatter(range(len(data)), data, color='blue', label='Original Data')

# Z-Scores
plt.plot(range(len(data)), z_scores_result, color='red', label='Z-Scores', linestyle='--', marker='o')

# Highlighting Anomalies (e.g., Z-Score > 2 or Z-Score < -2)
anomalies = np.where((np.abs(z_scores_result) > 1))

print(anomalies)

plt.scatter(anomalies, data[anomalies], color='orange', label='Anomalies', marker='X')

# Adding labels and legend
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('Z-Scores Visualization')
plt.legend()

# Show plot
plt.show()