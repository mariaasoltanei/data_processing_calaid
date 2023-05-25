import numpy as np
import matplotlib.pyplot as plt

t0 = 0
t1 = 20
n_samples = 1000

xs = np.linspace(t0, t1, n_samples)
# Generate signal with amplitudes 7 and 3
ys = 7*np.sin(15 * 2 * np.pi * xs) + 3*np.sin(13 * 2 * np.pi * xs)

np_fft = np.fft.fft(ys)
amplitudes = 2 / n_samples * np.abs(np_fft) 
print(amplitudes)

