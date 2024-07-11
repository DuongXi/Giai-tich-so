import numpy as np
import math
EPS = 0.001

def lenVoi(matrix):
    e = []
    
    global n
    for i in range(n):
        if mex !=[] and i == mex[-1]:
            e.append([0])
        else:
            e.append([1])
    x = matrix@e
    x1 = np.array(e)
    print(x)
    if mex != []:
        a = np.delete(x,mex,0)
        b = np.delete(x1,mex,0)
    else:
        a=x
        b=x1
    i = 0
    if len(mex) != n-1:
        while abs(sum(np.diff(np.transpose(a)/np.transpose(b))[0])) >= 0.01:
            x2 = x1
            x1 = x
            x = matrix@x
            print(f"Lần lặp {i+1}:",np.transpose(x))
            i+=1
            if mex != []:
                a = np.delete(x,mex,0)
                b = np.delete(x1,mex,0)   
            else:
                a=x
                b=x1
            if i > 40:
                break
    else:
        for i in range(20):
            x2 = x1
            x1 = x
            x = matrix@x
            # print(f"Lần lặp {i+1}:",np.transpose(x))

    x0 = list(abs(x))
    mex.append(x0.index(max(x0)))
    if i < 40:
        eigValue1 = x[mex[-1]]/x1[mex[-1]]
        eigVector1 = x/x[mex[-1]]
    else:
        eigValue1 = x[mex[-1]]/x2[mex[-1]]
        eigVector1 = x/x[mex[-1]]
    for i in range(len(eigVector1)):
        rounder = round(eigVector1[i][0],3)
        if (eigVector1[i,0] - rounder) < EPS:
            eigVector1[i,0] = rounder
    # eigVector1 = np.linalg.inv(theta)@eigVector1
    print(eigValue1[0])
    print(math.sqrt(eigValue1[0]))
    v.append(eigValue1)
    vec.append(list(eigVector1))
    eigVector2 = eigVector1/np.linalg.norm(eigVector1)
    print(eigVector2)
    return eigVector1

def xuongCho(matrix,x1,mex):
    global theta
    
    for i in range(n):
        theta[i,mex] -= x1[i]
    matrix = theta@matrix
    print("ma traanj:",matrix)
    return matrix

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

# main--------------------------------------------------------------------------------------
if __name__ == "__main__":
    v=[]
    vec=[]
    matrix = np.loadtxt("data.txt")
    mat = matrix.copy()
    n = len(matrix)
    i=0
    mex = []
    eigvector = []
    theta = np.eye(n)
    e = np.eye(n)
    m = np.zeros(n).reshape(-1,1)
    while(i<n):
             x1 = lenVoi(matrix)
             matrix = xuongCho(matrix, x1, mex)
             i+=1
    print("Các giá trị riêng: ", v)
    print("Các vector riêng: ", vec)
#     for i in v:
#         a = mat - i*e
#         a = np.hstack([a, m])
#         a = gaussThuan(a)
# print(eigvector)