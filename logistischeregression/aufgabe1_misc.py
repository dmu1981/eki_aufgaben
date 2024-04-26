import numpy as np
from matplotlib import pyplot as plt

def zeichnen(model, coords_x1, coords_x2, class_y):
    blue_indices = (class_y < 0.5)
    red_indices = (class_y > 0.5)

    plt.clf()
    w0, w1, w2, w3, w4, w5 = model[0], model[1], model[2], model[3], model[4], model[5]
    x1, x2 = np.meshgrid(np.linspace(-2,2,50), np.linspace(-2,2,50))
    z = w0 + w1 * x1 + w2 * x2 + w3 * (x1 ** 2) + w4 * (x2 ** 2) + w5 * x1 * x2
    z = np.clip(z, -1, 1)
    plt.contourf(x1, x2, z, levels=np.linspace(-1,1,20), cmap="coolwarm", alpha=.2)
    plt.contour(x1, x2, z, levels=[0.0], colors=["k"])
    plt.plot(coords_x1[blue_indices], coords_x2[blue_indices], 'bo')
    plt.plot(coords_x1[red_indices], coords_x2[red_indices], 'ro')


    plt.xlim((-1,1))
    plt.ylim((-1,1))