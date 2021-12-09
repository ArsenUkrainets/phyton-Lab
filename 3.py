import numpy as np
import matplotlib.pyplot as plt

# 1
plt.xlabel('axis X')
plt.ylabel("axis Y")
n = np.linspace(0, 2 * np.pi)
x = np.pi / 4
y = (n * x / np.sin(n * x))
plt.plot(n, y)
plt.show()

# 2
plt.xlabel('axis X')
plt.ylabel("axis Y")
x = np.linspace(-10, -1)
g = -x * 2 - 4 * x - 3
plt.plot(x, g)
x = np.linspace(-1, 1)
g = x + 1
plt.plot(x, g)
x = np.linspace(1, 10)
g = x / 2
plt.plot(x, g)
plt.show()
