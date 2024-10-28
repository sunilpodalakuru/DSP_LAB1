import numpy as np
import matplotlib.pyplot as plt
import librosa as lb
y,sr=lb.load("input.wav")
fs=900
x=y[::int(0.5*fs)]
N=len(x)
f=[]
k1=np.arange(0,N)
omega=np.arange(0,2*np.pi,(2*np.pi/len(x)))
for i in range(0,N):
    X=[]
    for k in range(0,N):
        a=x[k]*np.exp(-1j*(2*np.pi*k*i)/N)
        X.append(a)
    f.append(sum(X))
# print(f)
plt.stem(k1,np.abs(f))
plt.show()