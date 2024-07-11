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
    
def Seidel(b,d,eps,ep):
    x0=d
    print("Giá trị ban đầu:", x0)
    x1 = d-d
    b1 = np.tril(b)
    b2 = b-b1
    exp = 10
    c=1
    
    while exp >= eps:
        for i in range(len(b)):
            for j in range(len(b)):
                if(i>=j):
                    x1[i] += b1[i,j]*x1[j]
                else:
                    x1[i] += b2[i,j]*x0[j]
            x1[i]+=d[i]
            
        print(f"Lần lặp:{c}")
        print(x1)
        if Troi == 1:
            exp = (ep/(1-ep))*(np.linalg.norm(x1-x0, ord=np.inf))
        elif Troi == 2:
            exp = (ep/(1-ep))*(np.linalg.norm(x1-x0, ord=1))
        x0=x1
        x1=d-d
        c+=1
        print(f"Sai số:{exp}")
        
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
    ep = []
    
    for i in range(size):
        s= sum(abs(b[i,i:size]))
        t= sum(abs(b[i,0:i]))
        # print(s)
        # print(t)
        ep.append((s/(1-t)))
    ep = max(ep)
    print(ep)
    Seidel(b,d,eps,ep)

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

# main--------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    eps = float(input("Nhap sai so: "))
    # addIdentityMat(matrix)
    Troi = CheoTroiCheck(matrix)
    if Troi == 1:
        print("Ma trận đã cho là chéo trội hàng")
        eps = float(input("Nhap sai so: "))
        nghiem = config(matrix,eps)
    elif Troi == 2:
        print("Ma trận đã cho là chéo trội cột")
        eps = float(input("Nhap sai so: "))
        nghiem = config(matrix,eps)
    else:
        print("Ma trận không chéo trội, chọn pp khác đi")
         
    # addIdentityMat(matrix)
    print("Nghiệm của phương trình là: \n", nghiem)
    
    # print(matrix)