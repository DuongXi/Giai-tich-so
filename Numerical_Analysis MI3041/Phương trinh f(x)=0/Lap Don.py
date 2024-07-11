import math
import numpy as np
deltaX = 0.0000001

def khoangPhanLy():
    a1 = f(-10)
    a = np.linspace(-10,10,101)
    c = 0
    for index,i in enumerate(a):
        a2 = f(i)
        if a1 * a2 < 0:
            HeSo[c].append(a[index-1])
            HeSo[c].append(i)
            HeSo.append([])
            c += 1
        a1 = a2
        
def f(x):
    return pow((12*x+5),1/3)
    #return math.sin(x)
    #return math.log(x)-1
    #return pow(x,n) - a
    #return pow(x,5) - math.log((pow(x,2))) + pow(2,x)
def inp():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = input()
    LapDon(a, b, eps)

def outp(x,i):
    print("n = {}, x_{} = {}".format(i,i,round(x,8)))
    
def LapDon(a, b, eps):
    x = a
    i=0
    if fphay(b) >= 1:
        return 0
    else:
        q = fphay(b)
        while eps1>float(eps):
            x1 =f(x)
            i+=1
            outp(x1,i)
            eps1 = (q/(1-q))*abs(x1-x)
            print(f"Sai số: {eps1}")
            x = x1
def fphay(x):
    return (f(x+deltaX)-f(x))/deltaX

def f2phay(x):
    return (fphay(x+deltaX)-fphay(x))/deltaX

HeSo = [[]]     
khoangPhanLy()
print(HeSo)
inp()