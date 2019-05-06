import numpy as np
import os
import matplotlib.pyplot as plt
os.environ['PROJ_LIB'] = r'/anaconda3/pkgs/proj4-5.2.0-h0a44026_1/share/proj'
from mpl_toolkits.basemap import Basemap
import geopy
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.tan(x)
plt.title("sine wave form")

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()

plt.figure(figsize=(10,5))
world = Basemap()
world.drawcoastlines(linewidth=0.25,color="red")
world.drawcountries(linewidth=0.25)
plt.show()