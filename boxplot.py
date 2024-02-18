import matplotlib.pyplot as plt

# Toy sizes (replace with your actual data)
toy_sizes = [5, 7, 8, 10, 12, 15, 18, 20, 25, 30, 40, 50, 60]

# Create a box plot
plt.boxplot(toy_sizes,vert=0)

# Add labels and title
plt.xlabel('Toys')
plt.ylabel('Sizes')
plt.title('Box Plot of Toy Sizes')

# Show the plot
plt.show()
