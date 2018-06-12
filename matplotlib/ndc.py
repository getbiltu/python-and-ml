import numpy as np
import matplotlib.pyplot as plt
def pdf(s,m):
    sigmasq=s
    mu=m
    x=np.arange(-5,5,.1)
    y=1/np.sqrt(2*np.pi*sigmasq)*np.exp(-((x-mu)**2)/(2*sigmasq))
    print(x)
    print(y)
    plt.title("Probability density Function")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    value="sigma square=",sigmasq,"MU=",mu
    plt.text(0,.5,value)
    plt.plot(x,y)
    plt.show()

print("Enter The Value Of Sigma Square And MU:")
pdf(float(input()),float(input()))

