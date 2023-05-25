import numpy as np

def gaussJordan(matrix):
    count = -1.0
    index = []
    left = []
    print("Các bước bién dổi")
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
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I
            
def result(matrix):
    #giải nghiệm và ỉn ra kết quả
    kq = []
    for i in range(len(matrix)):
        x = matrix[i,len(matrix)]/matrix[i,i]
        kq.append(x)
    print("Nghiệm của hệ phương trình là: ")
    print(kq)

# main--------------------------------------------------------------------------------------
file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
# addIdentityMat(matrix)
gaussJordan(matrix)
result(matrix)

