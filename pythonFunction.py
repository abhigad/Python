def normalize1(x):
     return [(value - min(x)) / (max(x) - min(x)) for value in x]

def normalize(x):
    # Calculate min and max values in the list
    min_val = min(x)
    max_val = max(x)
    
    # Check if there is a range to normalize
    if max_val != min_val:
        # Use list comprehension to perform element-wise normalization
        normalized_data = [(value - min_val) / (max_val - min_val) for value in x]
        return normalized_data
    else:
        # Handle the case where all elements in the list are the same
        return x

# Example data
data = [10, 18, 20, 30, 70, 44, 50]

# Call normalize function
normalized_data = normalize1(data)

# Print the results
print("Original Data:", data)
print("Normalized Data:", normalized_data)
