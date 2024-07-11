import math
import numpy as np
deltaX = 0.0000001

def f(x):
    # return pow(x,3)+2*x-11
    return math.tan(x/4)-1
    #return math.log(x)-1
    #return pow(x,n) - a
    #return pow(x,5) - math.log((pow(x,2))) + pow(2,x)
    # return x**5 - 3*x**3+2*x**2-x+5

def inp():
    a = float(input("a = "))
    b = float(input("b = "))
    d = float(input("Điểm Fourier d = "))
    eps = input("Sai số:")
    DayCung(a, b,d, eps)

def outp(x1,x,i):
    print("n = {}, x_{} = {}, deltaX = {}".format(i,i,round(x,8),abs(x1-x)))
    
def DayCung(a, b, d, eps):
    m = fphay(a)
    n = fphay(b)
    x = b
    i=0
    eps1=10
    while eps1>float(eps):
            x1 = x - ((f(x)*(d-x))/(f(d)-f(x)))
            i+=1
            outp(x1,x,i)
            eps1 = ((n-m)/m)*abs(x1-x)
            print(f"Sai số: {eps1}")
            x = x1
def fphay(x):
    return (f(x+deltaX)-f(x))/deltaX

def f2phay(x):
    return (fphay(x+deltaX)-fphay(x))/deltaX

inp()