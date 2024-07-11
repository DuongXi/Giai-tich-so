import numpy as np

def Lapdon(b,d,eps):
    #thực hiện lặp đơn
    e = np.eye(size)
    b = e-b
    ep = 100
    x = d
    chuan = 0
    q = np.linalg.norm(b, ord=np.inf)
    
    if q>1:
        q = np.linalg.norm(b, ord=1)
        chuan = 1
    i=1
    
    while ep >= eps:
        x1= b@x+d
        print(f"Lần lặp:{i}")
        print(x1)
        if chuan == 1:
            q = np.linalg.norm(b, ord=1)
        else:
            ep = (q/(1-q))*(np.linalg.norm(x1-x, ord=np.inf))
        x=x1
        i+=1
        print(f"Sai số:{ep}")
    return x1

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I
    
# main--------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    # addIdentityMat(matrix)

    size = len(matrix)
    eps=float(input("Nhap sai so: "))
    
    b = matrix[0:size,0:size]
    d = matrix[0:size,size]
    nghiem = Lapdon(b,d,eps)
    
    print("\nNghiệm của phương trình là: ", nghiem)