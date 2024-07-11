import numpy as np

def Lobaxepski(i):
    n = len(i)
    x1 = i.copy()
    x2 = i.copy()   
    count = 0
    while(count<5):                   #   math.log10(abs(x1[n-1])) < 100
        for j in range(n):
            if j==0 or j==n-1:
                x1[j] = i[j]**2
            else:
                for k in range(0,n):
                    if k==0:
                        x1[j] = i[j]**2
                    elif j-k < 0 or j+k >= n:
                        continue
                    elif k % 2 != 0:
                        x1[j] -= 2*i[j-k]*i[j+k]
                    elif k % 2 == 0:
                        x1[j] += 2*i[j-k]*i[j+k]
        count+=1
        print(x1)
        i = x1.copy()
        
    for j in range(n):
        if j == 0:
            i[j] = i[j]**(1/2**count)
        else:
            i[j] = (i[j]/x1[j-1])**(1/2**count)
    i = i[1:n]
    
    for j in range(n-1):
        a = 0
        for k in range(1,n+1):
            a +=  ((-i[j])**(n-k))*x2[k-1]
        if a <= eps and a >= -eps:
            i[j] = -i[j]
    print("Các nghiệm của phương trình là: ",i)
    return i

# main------------------------------------------------------------------------------------
if __name__ == "__main__":
    eps = 1
    HeSo = [1.,-20.,0.,0.,3.,0.,-15.]
    # HeSo = [1., -4.0, -40.0, -56.0, -20.0]
    Lobaxepski(HeSo)
    print(HeSo)