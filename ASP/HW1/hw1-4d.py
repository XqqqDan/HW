import numpy as np
import matplotlib.pyplot as plt

x_n = [0, 0, 1, 2, 1, -1, -2, -1]
X_ejw = np.fft.fft(x_n, n=256)
x1 = np.abs(X_ejw)
x2 = np.angle(X_ejw)

plt.subplot(3, 1, 1)
plt.ylabel("DFT(x)")
plt.xlabel("n")
plt.stem(X_ejw)

plt.subplot(3, 1, 2)
plt.ylabel("Magnitude:X(ejω)")
plt.xlabel("Frequency:ω")
plt.stem(x1)

plt.subplot(3, 1, 3)
plt.ylabel("Phase:φ(ω)")
plt.xlabel("Frequency:ω")
plt.stem(x2)

plt.show()
