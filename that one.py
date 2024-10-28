X=[]
    for i in range(len(x)):
        y=[]
        for k in range(len(x)):
                 a=x[i]*(np.exp(-1j*2*np.pi*k*i/len(x)))	
                 y.append(a)
        X.append(sum(y))
    return(X)