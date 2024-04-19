import numpy as np
from matplotlib import pyplot as plt

# Einleitung
# #########
# Gegeben sind nun diese Daten
coords_x1 = np.random.normal(0, 0.5, 100) 
coords_x2 = np.random.normal(0, 0.5, 100)
class_y = 2.0 * ((coords_x1**2 + coords_x2**2) < 0.4) - 1.0


# Aufgabe 3a
# ##########
# Schätzen Sie ein Modell der Form 
#
#   y = w0 + w1 * x1 + w2 * x2 + w3 * x1^2 + w4 * x2^2 + w5*x1*x2
# 
# und zeichen Sie die Daten sowie die Trennfläche ihres Modells



## Bringen Sie diesen Code wieder ans Laufen um die Trennfläche zu visualieren
# x1, x2 = np.meshgrid(np.linspace(-2,2,50), np.linspace(-2,2,50))
# z = w0 + w1 * x1 + w2 * x2 + w3 * (x1 ** 2) + w4 * (x2 ** 2) + w5 * x1 * x2
# z = np.clip(z, -1, 1)
# print(np.min(z), np.max(z))
# blue_indices = (class_y < 0.0)
# red_indices = (class_y > 0.0)
# plt.contourf(x1, x2, z, levels=np.linspace(-1,1,20), cmap="coolwarm", alpha=.2)
# plt.contour(x1, x2, z, levels=[0.0], colors=["k"])
# plt.plot(coords_x1[blue_indices], coords_x2[blue_indices], 'bo')
# plt.plot(coords_x1[red_indices], coords_x2[red_indices], 'ro')


# plt.xlim((-1,1))
# plt.ylim((-1,1))
# plt.show()