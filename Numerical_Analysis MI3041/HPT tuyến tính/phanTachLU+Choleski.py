import numpy as np

def phanTachLU(matrix, L, U):
    #trả ma trận L,U và nghiệm hệ phương trình AX = b
    size = len(matrix)
    A = matrix[:size,:size]
    for i in range(0,size):
        if i == 0:
            L[:,i] = A[:,i]
            U[i,:] = A[i,:]/L[i,i]
        else:
            s1=0
            s2=0
            for j in range(0,i):
                s1 += U[j,i] * L[:,j]
                s2 += U[j] * L[i,j]
            L[:,i]= A[:,i] - s1
            U[i] = (A[i] - s2)/L[i,i]
    print("Ma trận L:\n", L)
    print("Ma trận U:\n", U)
    matrix[:size,:size] = L
    matrix[:,size] = daoGaussNghich(matrix)
    matrix[:size,:size] = U
    gaussNghich(matrix)

def choleski(matrix):
    #Thực hiện thuật toán choleski
    size = len(matrix)
    matL = np.zeros((size,size))
    matU = np.eye(size)
    phanTachLU(matrix, matL, matU)
    
def gaussNghich(matrix):
    #Tìm nghiệm hệ phương trình UX = y qua quá trình nghịch của thuật toán Gauss
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
    #Tìm nghiệm hệ phương trình LY = b qua quá trình nghịch của thuật toán Gauss nhưng ngược từ phương trình đầu xuống
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

#main-----------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")

    X = []
    Y = []
    # addIdentityMat(matrix)
    choleski(matrix)
    # phanTachLU(matrix)
    print("Nghiệm của hệ phương trình là: \n", X)