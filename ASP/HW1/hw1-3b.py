import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

yy = np.array([1, -3, 4, -12])
xx = np.array([2, 3, -1])

t, y = signal.dimpulse((xx, yy, 1), n=750)

plt.stem(t, np.squeeze(y))
plt.show()
