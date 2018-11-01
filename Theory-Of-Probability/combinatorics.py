#!/usr/bin/env python3
"""
One of the programs I've thrown together to make Dr. Montgomery's homework
go a little faster for me.
"""
import math
from math import factorial
from math import sqrt
import re

# The long way
def Choose(N,R):
    from math import factorial
    N = int(N)
    R = int(R)
    Cnumerator = factorial(N)
    Cdenominator = factorial(R) * factorial(N-R)
    Cresult = Cnumerator / Cdenominator
    print(N, 'Choose',R,'= ',Cresult,'different combinations.')
    return Cresult

# The short way
def c(n,r):
    from math import factorial
    n = int(n)
    r = int(r)
    Cnumerator = factorial(n)
    Cdenominator = factorial(r) * factorial(n-r)
    Cresult = Cnumerator / Cdenominator
    print(n, 'Choose',r,'= ',Cresult,'different combinations.')
    return Cresult
# The short way
def p(i,k):
    from math import factorial
    i = int(i)
    k = int(k)
    Pnumerator = factorial(i)
    Pdenominator = factorial(i-k)
    Presult = Pnumerator / Pdenominator
    print(i,'Permute',k,'= ',Presult,'different arrangements.')
    return Presult

# The long way
def Permute(I,K):
    from math import factorial
    I = int(I)
    K = int(K)
    Pnumerator = factorial(I)
    PdenomInator = factorial(I-K)
    Presult = Pnumerator / PdenomInator
    print(I,'Permute',K,'= ',Presult,'different arrangements.')
    return Presult
# Returns the probability of an event with a hypergeometric distribution
def Hypergeometric(rValue,yValue,NValue,nValue):
    numerator = Choose(rValue,yValue) * Choose(NValue - rValue, nValue - yValue)
    denominator = Choose(NValue, nValue)
    result = numerator / denominator
    print('The probability, P( Y =', yValue,') =', result)
    mu = nValue * rValue / NValue
    print(u'The mean \u03bc = Expected Value(Y) = ',mu)
    sigmaSquared = nValue * (rValue / NValue) * ((NValue - rValue)/NValue) * ((NValue - nValue)/(NValue - 1))
    print('The variance V(Y) =', sigmaSquared)
    sigma = sqrt(sigmaSquared)
    print(u'The standard deviation, for Y = any y, is \u03C3 =',sigma)
    return result

# After importing this file on the python terminal interpreter,
# having these object shortcuts reduces typing time
pi = math.pi
e = math.e
sin = math.sin
cos = math.cos
tan = math.tan
