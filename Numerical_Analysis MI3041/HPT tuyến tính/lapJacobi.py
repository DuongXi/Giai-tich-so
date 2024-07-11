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
    b = matrix[:,size]
    d = np.linalg.pinv(np.diag(np.diag(matrix[:,:size])))
    e = np.eye(size)
    B = -(d @ matrix[:,:size]-e)
    d = d@b
    ep = 100
    i=1
    q = np.linalg.norm(B, ord=np.inf)
    print(B)
    print(q)
    x = d - d
    while eps <= ep:
        x1 = B @ x + d
        print(f"Lần lặp:{i}")
        print(x1)
        ep = (q/(1-q))*(np.linalg.norm(x-x1, ord=np.inf))
        x = x1
        i += 1
        print(f"Sai số:{ep}")
    return x

def JacobiCot(matrix,eps):
    b = matrix[:,size]
    d = np.linalg.pinv(np.diag(np.diag(matrix[:,:size])))
    e = np.eye(size)
    B = -(d @ matrix[:,:size]-e)
    d = d@b
    ep = 100
    i=1
    q = np.linalg.norm(B, ord=1)
    print(B)
    print(q)
    x = d - d
    print(x)
    while eps <= ep:
        x1 = B @ x + d
        print(f"Lần lặp:{i}")
        print(x1)
        ep = (q/(1-q))*(np.linalg.norm(x-x1, ord=1))
        x = x1
        i += 1
        print(f"Sai số:{ep}")
    return x
    
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    size = len(matrix)
    print(matrix[:,:size])
    if np.linalg.det(matrix[:,:size]) == 0:
        print("Ma trận không khả nghịch, dừng thuật toán")   
        quit()
    Troi = CheoTroiCheck(matrix[:,:size])
    if Troi == 2:
        print("Ma trận A là chéo trội hàng")
        eps=float(input("Nhap sai so: "))
        nghiem = JacobiHang(matrix,eps)
    elif Troi == 1:
        print("Ma trận A là chéo trội cột")
        eps=float(input("Nhap sai so: "))
        nghiem = JacobiCot(matrix,eps)
    else:
        print(0)
    
    print("\nNghiệm của phương trình là: ", nghiem)