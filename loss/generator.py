import numpy as np
from matplotlib import pyplot as plt
import pickle

x = np.linspace(0, 1, 100)
y = 100.0 - 9.81 * x**2 + np.random.normal(0, 0.5, x.shape)
alpha = np.random.uniform(0.0, 1.0, x.shape) < 0.33
y = (1.0 - alpha) * y + alpha * (y + np.random.uniform(-10, 10, x.shape))

with open("data.pk", "wb") as f:
  f.write(pickle.dumps([x.reshape(-1,1),y]))

plt.plot(x,y,'.')
plt.show()
