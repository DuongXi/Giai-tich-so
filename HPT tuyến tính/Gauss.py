import numpy as np
def GaussThuan(matrix):
    for j in range(0,len(matrix)-1):
        for i in range(j+1,len(matrix)):
            if int(matrix[j,j])==0:
                swap(matrix,j)
            matrix[i] = matrix[i] - (matrix[i,j]/matrix[j,j])*matrix[j]
        # print(matrix)
            
def GaussNghich(matrix):
    size = len(matrix)
    for i in range(0,size):
        k=len(kq)-1
        sum = 0
        for j in range(size-i,size):
            sum += matrix[size-1-i,j]*kq[k]
            k-=1 
        n = ((matrix[size-1-i,size])-sum)/matrix[size-1-i,size-1-i]
        kq.append(n)
        
def swap(matrix,c):
    m=c
    for n in range(c+1,len(matrix)):
        if matrix[n,m] != 0:
            tmp = matrix[n].copy()
            matrix[n] = matrix[c]
            matrix[c] = tmp
        return


file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
kq = []
GaussThuan(matrix)
GaussNghich(matrix)
# print(matrix)
kq.reverse()
print(kq)