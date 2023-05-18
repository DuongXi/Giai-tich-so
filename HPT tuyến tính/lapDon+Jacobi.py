import numpy as np
import timeit
def Lapdon(b,d,eps):
    ep = 100
    x= d-d
    q = np.linalg.norm(b, ord=np.inf)
    if q>1:
        q = np.linalg.norm(b, ord=1)
    print(q)
    i=1
    while ep >= eps:
        x1= b@x+d
        print(f"Lần lặp:{i}")
        print(x1)
        ep = (q/(1-q))*(np.linalg.norm(x1-x, ord=np.inf))
        x=x1
        i+=1
        print(f"Sai số:{ep}")
        
def config(matrix,eps):
    diag = np.diag(matrix).copy()
    size = len(matrix)
    for i in range(0,size):
        for j in range(0, size+1):
            if j==i:
                matrix[i,j] = 0
            elif(j != i):
                if(j<size):
                    matrix[i,j] = matrix[i,j]/-diag[i]
                else:
                    matrix[i,j] = matrix[i,j]/diag[i]
    b = matrix[0:size,0:size]
    d = matrix[0:size,size]
    print(b)
    # print(d)
    Lapdon(b,d,eps)
    
# main--------------------------------------------------------------------------------------
file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
eps=float(input("Nhap sai so: "))
config(matrix,eps)
# print(matrix)