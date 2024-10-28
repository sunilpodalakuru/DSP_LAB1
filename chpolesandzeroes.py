# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # Coefficients of the numerator and denominator
# b = [1, -0.5]  # Example numerator coefficients
# a = [1, -1.2, 0.7]  # Example denominator coefficients

# # Find the poles and zeros
# zeros, poles, _ = signal.tf2zpk(b, a)

# # Plot poles and zeros
# plt.figure()
# plt.scatter(np.real(zeros), np.imag(zeros), s=50, facecolors='none', edgecolors='r', label='Zeros')
# plt.scatter(np.real(poles), np.imag(poles), s=50, facecolors='none', edgecolors='b', label='Poles')

# # Plot unit circle for reference
# unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
# plt.gca().add_artist(unit_circle)

# plt.axvline(0, color='gray', lw=1)
# plt.axhline(0, color='gray', lw=1)

# plt.xlabel('Real')
# plt.ylabel('Imaginary')
# plt.title('Pole-Zero Plot')
# plt.legend()
# plt.grid(True)
# plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Example poles and zeros
zeros = np.array([0.5 + 0.5j, -0.5 - 0.5j])
poles = np.array([0.8 + 0.6j, 0.8 - 0.6j, -0.9 + 0.1j])

plt.figure()

# Plot the zeros with red 'o' markers (unfilled circles)
plt.plot(np.real(zeros), np.imag(zeros), 'ro', markerfacecolor='none', label='Zeros')

# Plot the poles with blue 'x' markers
plt.plot(np.real(poles), np.imag(poles), 'bx', label='Poles')

# Plot unit circle for reference
unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
plt.gca().add_artist(unit_circle)

plt.axvline(0, color='gray', lw=1)  # Plot a vertical line at real=0 (y-axis)
plt.axhline(0, color='gray', lw=1)  # Plot a horizontal line at imag=0 (x-axis)

plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.title('Pole-Zero Plot using plt.plot()')
plt.legend()
plt.grid(True)
plt.show()
