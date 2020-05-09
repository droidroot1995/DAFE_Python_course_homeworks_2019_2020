def integr(x0,x1,n):
    s=0
    dx=(x1-x0)/n
    for i in range (n):
        s+=(np.exp(i*dx)*np.sin(i*dx)+np.exp((i+1)*dx)*np.sin((i+1)*dx))/2*dx
    return s
print(integr(0,1,100))  
