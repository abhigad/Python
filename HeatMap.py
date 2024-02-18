import pandas as pd
import matplotlib.pyplot as plt

print('hello')

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with the path to your CSV file

print(df)

# Create a heatmap using Matplotlib
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed

# Customize the heatmap using your DataFrame
heatmap = plt.imshow(df.values, cmap='coolwarm', aspect='auto')  # You can choose a different colormap

# Add a color bar
plt.colorbar(heatmap)

# Add labels for the x and y axes
plt.title('Abusive ASINs Per Category')
plt.xlabel('ASIN')
plt.ylabel('Category')

# Show the heatmap
plt.title('CSV Data Heatmap')
plt.show()
