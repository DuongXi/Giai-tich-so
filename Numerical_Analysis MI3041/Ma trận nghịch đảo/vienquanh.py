import numpy as np

def VienQuanh(matrix):
    n = len(matrix) 
    matrix[:2,:2]= np.linalg.inv(matrix[:2,:2])
    print(matrix[:2,:2])
    for i in range(2,n):
        alpha21 = matrix[i,:i]
        alpha12 = matrix[:i,i]
        alpha12 = np.transpose(alpha12)
        alpha22 = matrix[i,i]
        X = matrix[:i,:i]@alpha12
        Y = alpha21@matrix[:i,:i]

        theta = alpha22 - Y@alpha12
        matrix[:i,:i] = matrix[:i,:i] + (1/theta)*(X.reshape(-1,1)*Y)
        matrix[:i,i] = -X*(1/theta)
        matrix[i,:i] = -(1/theta)*Y
        matrix[i,i]= 1/theta
        print(f"Lần lặp {i}:\n",matrix[:i+1,:i+1])
   
    print("Ma trận nghịch đảo là: \n",matrix)
    

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I
    return matrix

# main--------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    # addIdentityMat(matrix)
    VienQuanh(matrix)
    # print(matrix)