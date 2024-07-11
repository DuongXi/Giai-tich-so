import numpy as np

def gaussJordan(matrix):
    count = -1.0
    index = []
    left = []
    print("Các bước bién đổi Gauss-Jordan:")
    for c in range(0, len(matrix)):
        left.append(c)
    for i in range(0, len(matrix)):
        #Kiểm tra, ưu tiên các phần tử đặc biệt 
        if matrix[i,i] == 1 and not(i in index):
            count = i
            index.append(count)
            break

        elif matrix[i,i] == -1 and not(i in index):
            count = i
            index.append(count)
            break

        elif abs(matrix[i,i]) == max(np.diag(abs(matrix))) and not(i in index):
            count = i
            index.append(count)
            break

    config(matrix,count)

    for count in left:
        if not(count in index):
            config(matrix,count)
    
    for j in range(0,len(matrix)):
        matrix[j] = matrix[j]/matrix[j,j]
    
    size = len(matrix)
    print("Ma trận nghịch đảo là:")
    print(matrix[:,size:size*2]) 

def merge(matrix):
    size = len(matrix)
    E = np.eye(size)
    AA = np.zeros((size,2*size))
    AA[:,:size] = matrix
    AA[:,size:2*size] = E
    gaussJordan(AA)

def config(matrix,count):
    #thực hiện biến đổi hàng
    for j in range(0,len(matrix)):
        if j == count:
            pass
        else:
            matrix[j] = matrix[j] - (matrix[j,count]/matrix[count,count])*matrix[count]
    print(matrix)
    print()

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị: "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

# main--------------------------------------------------------------------------------------
if __name__ == "__main__":

    matrix = np.loadtxt("data.txt")
    # for i in range (len(matrix)):
    #     matrix[i,i] += 100
    print(matrix)
    # addIdentityMat(matrix)
    gaussJordan(matrix)
    merge(matrix)