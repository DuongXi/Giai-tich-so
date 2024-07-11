import numpy as np
import math

def choleski(matrix):
    size = len(matrix)
    q = np.zeros((size,size))
    for i in range (size):
        if i == 0:
            q[i,i] = math.sqrt(matrix[i,i])
            if q[i,i] == 0:
                print("Ma trận A suy biến, không thoả mãn điều kiện")
                return
            q[i,1:] = matrix[i,1:]/q[i,i]
        else:
            q[i,i] = math.sqrt(matrix[i,i] - sum(q[0:i,i]**2))
            if q[i,i] == 0:
                print("Ma trận A suy biến, không thoả mãn điều kiện")
                return
            for j in range(i+1,size):
                q[i,j] = (matrix[i,j]-(q[0:i,i] @ np.transpose(q[0:i,j])))/q[i,i]
                
    matrix = np.transpose(q)
    matrix[:,size] = daoGaussNghich(matrix)
    matrix[0:size,0:size] = q
    gaussNghich(matrix)

def gaussNghich(matrix):
    #Tìm nghiệm hệ phương trình QX = y qua quá trình nghịch của thuật toán Gauss
    size = len(matrix)
    for i in range(0,size):
        k=len(X)-1
        sum = 0
        for j in range(size-i,size):
            sum += matrix[size-1-i,j]*X[k]
            k-=1 
        n = ((matrix[size-1-i,size]) - sum)/matrix[size-1-i,size-1-i]
        X.append(n)
    X.reverse()

def daoGaussNghich(matrix):
    #Tìm nghiệm hệ phương trình Q(t)Y = b qua quá trình nghịch của thuật toán Gauss nhưng ngược từ phương trình đầu xuống
    size = len(matrix)
    for i in range(0,size):
        sum = 0
        if i !=0:
            for j in range(0,i):
                sum +=matrix[i,j]*Y[j]
        n = (matrix[i,size]-sum)/matrix[i,i]
        Y.append(n)
    return Y

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

#main-----------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")

    X = []
    Y = []
    # addIdentityMat(matrix)
    choleski(matrix)
    print("Ma trận nghịch đảo là: \n",X)