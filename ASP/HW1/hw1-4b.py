import numpy as np
import matplotlib.pyplot as plt

w = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
X_ejw = (
    np.e ** ((0 + 1j) * w)
    + 2
    + np.e ** ((0 - 1j) * w)
    - np.e ** ((0 - 2j) * w)
    - 2 * np.e ** ((0 - 3j) * w)
    - np.e ** ((0 - 4j) * w)
)
x1 = np.abs(X_ejw)
x2 = np.angle(X_ejw)
plt.subplot(2, 1, 1)
plt.ylabel("Magnitude")
plt.xlabel("Frequency")
plt.plot(w, x1)
plt.subplot(2, 1, 2)
plt.ylabel("Phase")
plt.xlabel("Frequency")
plt.plot(w, x2)
plt.show()
