import pandas as pd
import numpy as np

np.random.seed(42)  # For reproducibility

# Function to generate synthetic location data for Maharashtra and Uttarakhand
def generate_location_data(num_points=100):
    # Maharashtra bounding box (latitude, longitude)
    maharashtra_box = {'latitude': (16.6, 20.9), 'longitude': (72.6, 80.9)}

    # Uttarakhand bounding box (latitude, longitude)
    uttarakhand_box = {'latitude': (28.8, 31.4), 'longitude': (77.2, 81.3)}

    # Simulating two movement categories: 'Tiger Movement' and 'No Movement'
    movement_labels = np.random.choice(['Tiger Movement', 'No Movement'], size=num_points)

    # Generate random locations for Maharashtra
    maharashtra_locations = pd.DataFrame({
        'latitude': np.random.uniform(*maharashtra_box['latitude'], size=num_points),
        'longitude': np.random.uniform(*maharashtra_box['longitude'], size=num_points),
        'movement_label': movement_labels
    })

    # Generate random locations for Uttarakhand
    uttarakhand_locations = pd.DataFrame({
        'latitude': np.random.uniform(*uttarakhand_box['latitude'], size=num_points),
        'longitude': np.random.uniform(*uttarakhand_box['longitude'], size=num_points),
        'movement_label': movement_labels
    })

    # Concatenate the two dataframes
    location_data = pd.concat([maharashtra_locations, uttarakhand_locations], ignore_index=True)

    return location_data

# Generate synthetic location data with 50 points per state
location_data = generate_location_data(num_points=50)

# Save the generated data to a CSV file
location_data.to_csv('tiger_movement_data1.csv', index=False)

# Display the first few rows of the generated data
print(location_data.head())
