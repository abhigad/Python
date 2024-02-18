import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import folium

# Load past movement data (replace with your dataset)
data = pd.read_csv('tiger_movement_data1.csv')

# Assuming your dataset has columns like 'latitude', 'longitude', and 'movement_label'
# Features are latitude and longitude, and the label is the movement category

# Features (latitude and longitude)
X = data[['latitude', 'longitude']]

# Label (movement category)
y = data['movement_label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier (replace with your preferred model)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Visualize the predicted movement on a map using folium
map_center = [data['latitude'].mean(), data['longitude'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Mark the actual movement locations
for index, row in data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['movement_label']).add_to(mymap)

# Mark the predicted movement locations
for idx, pred_label in enumerate(predictions):
    if pred_label == 'Tiger Movement':
        folium.CircleMarker([X_test.iloc[idx]['latitude'], X_test.iloc[idx]['longitude']],
                            radius=5,
                            color='red',
                            fill=True,
                            fill_color='red',
                            fill_opacity=0.7,
                            popup=f'Predicted: {pred_label}').add_to(mymap)

# Save the map to an HTML file
mymap.save('tiger_movement_prediction_map.html')
