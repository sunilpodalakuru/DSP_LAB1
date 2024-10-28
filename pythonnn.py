import numpy as np
import matplotlib.pyplot as plt
f=200
d=0.5
s=5000
t=np.arange(0,0.5,2500)
y=np.sin(2*np.pi*f*t)
plt.plot(t,y)
plt.show()