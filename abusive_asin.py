import pandas as pd
import random

# Create a sample dataset
data = {
    'ASIN': ['ASIN1', 'ASIN2', 'ASIN3', 'ASIN4', 'ASIN5'],
    'Category': ['Electronics', 'Books', 'Clothing', 'Toys', 'Health'],
    'Abuse_Score': [random.uniform(0, 1) for _ in range(5)]  # Generate random abuse scores between 0 and 1
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('abusive_data.csv', index=False)
