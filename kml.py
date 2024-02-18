import geopandas as gpd
import matplotlib.pyplot as plt

# gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'

# df = gpd.read_file('file.kml', driver='KML')

# Read the KML file
gdf = gpd.read_file('file.kml')
print(gdf.head())

# # Plot the data
# fig, ax = plt.subplots(figsize=(10, 10))
# gdf.plot(ax=ax, color='blue', edgecolor='black')
# plt.title('KML Visualization')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.show()
