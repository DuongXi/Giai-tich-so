import numpy as np

def Newton(eps):
    #thực hiện lặp đơn
    e = np.eye(n)
    ep = 100
    # X0 = np.array([[1],[0],[0],[0]])
    X0 =  np.transpose(matrix)/((np.linalg.norm(matrix))**2)
    # X0 =  np.transpose(matrix)/((np.linalg.norm(matrix,ord=1))*(np.linalg.norm(matrix,ord=np.inf)))
    G = e - matrix@X0
    print(G)
    q = np.linalg.norm(G, ord=np.inf)
    i=1
    if q >= 1:
        print(q)
        print("Chọn xấp xỉ đầu X0 khác đi")
        return 0
    while ep >= eps:
        X1 = X0@(2*e-matrix@X0) 
        print(f"Lần lặp:{i}")
        print(X1)
        ep = (q**2/(1-q))*(np.linalg.norm(X1, ord=np.inf))
        X0=X1
        G = e - matrix@X0
        q = np.linalg.norm(G, ord=np.inf)
        i+=1
        print(f"Sai số:{ep}")
    return X1

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

matrix = np.loadtxt("data.txt")
# addIdentityMat(matrix)
eps=float(input("Nhap sai so: "))
n = len(matrix)
i=0
mex = []
e = np.eye(n)
mat = Newton(eps)
print("Ma trận nghịch đảo là: \n",mat)