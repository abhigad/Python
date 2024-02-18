import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
df = pd.read_csv('abusive_data.csv')  # Replace with your actual file path

# Pivot the data to create a heatmap
heatmap_data = df.pivot(index='Category', columns='ASIN', values='Abuse_Score')

# Create the heatmap using Seaborn
plt.figure(figsize=(10, 10))
 
sns.heatmap(heatmap_data, vmin=0.1, vmax=1.0, annot=True, fmt=".3f", cbar_kws={'label': 'Abuse Score'})

plt.title('Abusive ASINs Per Category')
plt.xlabel('ASIN')
plt.ylabel('Category')

plt.show()
