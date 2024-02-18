import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

# Function to generate random movement data
def generate_movement_data(num_points=100):
    latitudes = np.random.uniform(10.0, 15.0, num_points)
    longitudes = np.random.uniform(70.0, 80.0, num_points)
    
    # Simulating two movement categories: 'Tiger Movement' and 'No Movement'
    movement_labels = np.random.choice(['Tiger Movement', 'No Movement'], size=num_points)
    
    return pd.DataFrame({'latitude': latitudes, 'longitude': longitudes, 'movement_label': movement_labels})

# Generate synthetic tiger movement data with 200 points
tiger_movement_data = generate_movement_data(num_points=200)

# Save the generated data to a CSV file
tiger_movement_data.to_csv('tiger_movement_data.csv', index=False)

# Display the first few rows of the generated data
print(tiger_movement_data.head())
