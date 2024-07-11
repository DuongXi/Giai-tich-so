import numpy as np

def CheoTroiCheck(matrix):
    n = len(matrix)
    Troi = 0
    sumC = []
    for i in range(n):
        check = sum(abs(matrix[i]))- matrix[i][i]
        sumC.append(check)
        if check - matrix[i][i] >= 0:
            break
        else:
            sumC.append(check)
            
    if i == n-1:
        Troi = 1
        return Troi
    sumC = []
    for j in range(n):
        check = sum(abs(matrix[:,j]))- matrix[j][j]
        sumC.append(check)
        if check - matrix[j][j] >= 0:
            break
        else:
            sumC.append(check)

    if j == n-1:
        Troi = 2
        return Troi
    
def JacobiHang(matrix,eps):
    size = len(matrix)
    d = np.linalg.pinv(np.diag(np.diag(matrix)))
    e = np.eye(size)
    b = -(d @ matrix-e)
    ep = 100
    i=1
    q = np.linalg.norm(b, ord=np.inf)
    print(b)
    print(q)
    while eps <= ep:
        x = b @ matrix + d
        print(f"Lần lặp:{i}")
        print(x)
        ep = (q/(1-q))*(np.linalg.norm(x-matrix, ord=np.inf))
        matrix = x
        i += 1
        print(f"Sai số:{ep}")
    return matrix

def JacobiCot(matrix,eps):
    size = len(matrix)
    d = np.linalg.pinv(np.diag(np.diag(matrix)))
    e = np.eye(size)
    b = e - (d @ matrix)
    ep = 100
    i=1
    q = np.linalg.norm(b, ord=1)
    print(b)
    print(d)
    while eps <= ep:
        x = b @ matrix + d
        print(f"Lần lặp:{i}")
        print(x)
        ep = (q/(1-q))*(np.linalg.norm(x-matrix, ord=1))
        matrix = x
        i += 1
        print(f"Sai số:{ep}")
    return matrix

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I
    return matrix
    
#main-----------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    matrix = addIdentityMat(matrix)
    print(matrix)
    if np.linalg.det(matrix) == 0:
        print("Ma trận không khả nghịch, dừng thuật toán")   
        quit()
    Troi = CheoTroiCheck(matrix)
    if Troi == 1:
        print("Ma trận đã cho là chéo trội hàng")
        eps=float(input("Nhap sai so: "))
        inv = JacobiHang(matrix,eps)
    elif Troi == 2:
        print("Ma trận đã cho là chéo trội cột")
        eps=float(input("Nhap sai so: "))
        inv = JacobiCot(matrix,eps)
    else:
        print("Ma trận không chéo trội, chọn pp khác đi")
        quit()
        
    # addIdentityMat(matrix)
    print("Ma trận nghịch đảo là: \n", inv)