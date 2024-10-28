import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    f=[]
    N=len(x)
    for i in range(0,N):
        X=[]
        for k in range(0,N):
            a=x[k]*np.exp(-1j*(2*np.pi*k*i)/N)
            X.append(a)
        f.append(sum(X))
    return f
x=[10,20,30,40,50,60,70,80,90,100]
y=dft(x)
k=np.arange(0,2*np.pi,(2*np.pi/len(x)))
# print(y)
plt.subplot(1,2,1)
plt.stem(k,np.abs(y))
# plt.plot(k,np.abs(y))
n=int(input("Enter No.of Zeroes to be padded: "))
for i in range(0,n):
    x.append(0)
y1=dft(x)
k1=np.arange(0,2*np.pi,(2*np.pi/len(x)))
plt.subplot(1,2,2)
plt.stem(k1,np.abs(y1))
# plt.plot(k1,np.abs(y1))
plt.show()

