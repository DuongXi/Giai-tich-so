import numpy as np
import math

eps = 0.1

def Danielevsky(matrix):
    eps = 10**-6
    n = len(matrix)
    m = np.eye(n,n)
    k = n-1
    i = [1]
    l = np.eye(n,n)
    while(k > 0):
        if(int(matrix[k,k-1]) == 0 and k > 1):
            swap(matrix,k)
            m[k-1] = matrix[k]
            l = l @ np.linalg.pinv(m)
            matrix = m @ matrix @ np.linalg.pinv(m)
            m = np.eye(n,n)
            k -= 1
        else:
            m[k-1] = matrix[k]
            l = l @ np.linalg.pinv(m)
            matrix = m @ matrix @ np.linalg.pinv(m)
            m = np.eye(n,n)
            k -= 1
        print(matrix)
    # print(matrix)
        
    for j in range(n):
        i.append(-round(matrix[0,j],3))
    print(i)
    # i=[1,0,0,-1]
    i = findEiValue(i)
    v = findEiVector(i,n,l)
    return i,v
        
def swap(matrix,k):
    n = len(matrix)
    for j in range(n):
        if(matrix[k,j] != 0):
            tmp = matrix[:,j]
            matrix[:,j] = matrix[:,k] 
            matrix[:,k] = tmp 

def findEiValue(i):     #Trả về trị riêng dùng phương pháp lobasepski 
    n = len(i)
    x1 = i.copy()
    x2 = i.copy()
    count = 0
    while(count<4):                   #   math.log10(abs(x1[n-1])) < 100
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
    print("Giá trị riêng của ma trận là: ",i)
    return i

def findEiVector(i,n,l):
    eiVector = []
    for eiVal in i:
        v = []
        for j in range(n):
            v.append(eiVal**(n-j-1))
        v = l @ v
        eiVector.append(v)
    return eiVector


def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I
# main------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    Danielevsky(matrix)
    # addIdentityMat(matrix)