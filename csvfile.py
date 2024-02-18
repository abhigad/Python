import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': np.random.rand(5),
    'B': np.random.rand(5),
    'C': np.random.rand(5),
    'D': np.random.rand(5),
}

df = pd.DataFrame(data)
print(df)

# Save the DataFrame to a CSV file
df.to_csv('c:/abhi/python/your_data.csv', index=False)