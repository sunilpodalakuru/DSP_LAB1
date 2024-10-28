import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    X=[]
    for i in range(len(x)):
        y=[]
        for k in range(len(x)):
            y.append(x[i]*(np.exp(-1j*2*np.pi*k*i/len(x))))
        X.append(sum(y))
    return(X)

x=[6,4,3,8,1,0,12,3]
y=dft(x)
k=np.arange(0,2*np.pi,(2*np.pi/len(x)))
plt.plot(k,np.abs(y))
plt.show()
for i in range(0,5):
    x.append(0)
y1=dft(x)

