import numpy as np

def Lapdon(b,d,eps):
    #thực hiện lặp đơn
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
    #thực hiện biến đổi trong lặp Jacobi
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
    
def isDiagonallyDominant(matrix):
    #Kiểm tra chéo trội hay không
    check=0
    s = len(matrix)
    for i in range (0,s):
        if matrix[i,i] > sum(matrix[i,0:s])- matrix[i,i]:
            check+=1
    return check == s

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

# main--------------------------------------------------------------------------------------
file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
# addIdentityMat(matrix)
if isDiagonallyDominant(matrix):
    eps=float(input("Nhap sai so: "))
    config(matrix,eps)
else:
    print("Ma trận không chéo trội nên hãy dùng phương pháp ngoài cái này nhé !!")
