import numpy as np
import matplotlib.pyplot as plt
b=[1,-0.5]
a=[1,-1.2,0.7]
zeroes=np.roots(b)
poles=np.roots(a)
print(np.roots(b))
print(np.roots(a))
plt.plot(np.real(zeroes),np.imag(zeroes),'ro',label="zeroes")
plt.plot(np.real(poles),np.imag(poles),'bx',label="poles")
plt.grid(True)
plt.legend()
plt.show()
