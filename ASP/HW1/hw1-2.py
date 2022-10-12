import numpy as np
import matplotlib.pyplot as plt

h = np.array([2, -3, 1])
len_h = len(h)
flag_h = 0
x = np.array([1, 2, 1, -1, -2, -1])
len_x = len(x)
flag_x = -1
axis_y = np.convolve(h, x)
len_y = len_x + len_h - 1
flag_y = flag_x + flag_h
axis_x = np.arange(flag_y, len_y + flag_y)

plt.subplot(2, 1, 1)
plt.stem(axis_x, axis_y)

N = 2 ** (int(np.log2(len_y)) + 1)
fft_x = np.fft.fft(x, N)
fft_h = np.fft.fft(h, N)

yy = np.fft.ifft(fft_x * fft_h)
axis_x2 = np.arange(flag_y, len(yy) + flag_y)
plt.subplot(2, 1, 2)
plt.stem(axis_x2, yy)

plt.show()
