import math
import numpy as np
deltaX = 0.0000001

def f(x):
    return x**3+2*x-11
    #return math.sin(x)
    #return math.log(x)-1
    #return pow(x,n) - a
    #return pow(x,5) - math.log((pow(x,2))) + pow(2,x)
    
def inp():
    a = float(input("a = "))
    b = float(input("b = "))
    x0 = float(input("Diem x0 bat ki thuoc [a,b]: "))
    eps = float(input("Sai số"))
    TiepTuyen(a, b, x0, eps)

def outp(x1,x,i):
    print("n = {}, x_{} = {}, deltaX = {}".format(i,i,round(x,8),abs(x1-x)))
    
def TiepTuyen(a, b, x0, eps):
    i=0
    eps1=10
    while eps1>float(eps):
        x1 = x0 - f(x0)/fphay(x0)
        i+=1
        outp(x1,x0,i)
        eps1 = (fphay(x0)/f2phay(x0))*((x1-x0)**2)
        print("Sai số",eps1)
        x0 = x1
        
def fphay(x):
    return (f(x+deltaX)-f(x))/deltaX

def f2phay(x):
    return (fphay(x+deltaX)-fphay(x))/deltaX
# ---------------------------
inp()