from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

main_path = Path().absolute()
data_path = main_path / "Data" / "Clean"

file_name = "u_v_coordinates.csv"
file_path = data_path / file_name
if not file_path.is_file():
    raise FileNotFoundError(f"File {file_name} does not exist!")


df = pd.read_csv(file_path)
# Extract the columns you need into NumPy arrays
coordinates = df[["_v [meter]", "_u []"]].to_numpy()
values = df[["NearETotal/max(NearETotal) []"]].to_numpy()

# Plot the image
plt.figure(figsize=(8, 6))
plt.scatter(coordinates[:, 0], coordinates[:, 1], c=values[:, 0], cmap='rainbow')
plt.colorbar(label='Image values')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Original Image Plot')
plt.show()

# Smoothing the values using 2D kernel density estimation (KDE) with adjustable bandwidth
bandwidth = 0.9  # Adjust this value to control the level of smoothing
kde = stats.gaussian_kde(coordinates.T, weights=values[:, 0], bw_method=bandwidth)
x_min, x_max = coordinates[:, 0].min(), coordinates[:, 0].max()
y_min, y_max = coordinates[:, 1].min(), coordinates[:, 1].max()
X, Y = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
Z = kde(np.vstack([X.ravel(), Y.ravel()]))

# Contour plot of the smoothed image
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z.reshape(X.shape), cmap='rainbow')
plt.colorbar(label='Smoothed Image values')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Smoothed Image Plot')
plt.show()
