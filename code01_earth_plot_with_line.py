# Demonstrating use of matplotlib.patches.Circle() function
# to plot an un-colored Circle
#pip install matplotlib
#sudo apt-get install python3-tk

earth_r_mi=3958.8
r=earth_r_mi*1.609344


import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 150)

radius = r
print('Earth Radius=',r,'km')
a = radius * np.cos(theta)
b = r+radius * np.sin(theta)


figure, axes = plt.subplots(1)


x1 = np.array([-r, 0, r])
y1 = np.array([0, 0, 0])

axes.plot(x1,y1,color = 'r')


axes.plot(a, b,color = 'b')
axes.set_aspect(1)

plt.title('Parametric Equation Circle')
plt.show()
