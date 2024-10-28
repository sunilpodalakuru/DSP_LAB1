import numpy as np
x=[1,2,3,4]
n=np.arange(len(x))
z=np.linspace(0.5,2,100)
z_t=[np.sum(x*(i**(-n))) for i in z]
print(z_t)