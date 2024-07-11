import math
import numpy as np

def f(x):
    #return x-1.25
    # return math.log(x)-1
    #return pow(x,n) - a
    #return pow(x,5) - math.log((pow(x,2))) + pow(2,x)
    return x**6-80
        
def inp():
    a = float(input("a = "))
    b = float(input("b = "))
    eps = float(input("Sai số: "))
    chiaDoi(a,b,eps)
    
def outp(a,b,x,i):
    print("a_{} = {}, b_{} = {}, x_{} = {}, f(x_{}) = {}".format(i,a,i,b,i,round(x,8),i,f(x)))
    
def chiaDoi(a,b,eps):
    i = 0
    print("1. Hậu nghiệm")
    print("2. Tiên nghiệm")
    ch = input("Chọn công thức tính sai số: ")
    if ch == '1':
        eps1 = 10
        while eps1 > float(eps):
            x = (a + b)/2
            if f(x) == 0:
                outp(a,b,x,i)
                return 0
            else:
                if f(a)*f(x) < 0:
                    c=b
                    b=x
                    outp(a,c,x,i)
                else:
                    c=a
                    a=x
                    outp(c,b,x,i)
            # công thức hậu nghiệm
                eps1 = abs(b-a)
                print(f"Sai số là: {eps1}")
                i+=1
                
    elif ch == '2':
        n = int(math.log2(abs(b-a)/eps)) + 1
        print("Số lần lặp là:", n)
        for i in range(n):
            x = (a + b)/2
            if f(x) == 0:
                outp(a,b,x,i)
                return 0
            else:
                if f(a)*f(x) < 0:
                    c=b
                    b=x
                    outp(a,c,x,i)
                else:
                    c=a
                    a=x
                    outp(c,b,x,i)
        print(f"Sai số là: {eps}")

# khoangPhanLy()
inp()