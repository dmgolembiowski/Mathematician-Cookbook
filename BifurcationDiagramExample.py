import numpy as n
import scipy as s
import matplotlib.pylab as p #pylab is part of matplotlib

# For the logistic map Xn+1 = rXn(1-Xn)
X0=0.252 # x-naught
xb=1.99 # upper bound on X

#Calling signatures for placing a legend on the axes
#legend()
#legend(labels)
#legend(handles, labels)

C=n.linspace(X0,xb,100)
print(C)
iter=1000
Y = n.ones(len(C))

for x in range(iter):
    Y = Y**2 - C   #get rid of early transients
    p.plot(C,Y, '.', color = 'k', markersize = 2)

#for x in range(iter): 
#    Y = Y**2 - C
#    p.plot(C,Y, '.', color = 'k', markersize = 2)

p.show()