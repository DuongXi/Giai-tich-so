import numpy as np
eps = 0.0001

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
    s = len(matrix)
    for i in range(s):
        for j in range(s):
            if abs(matrix[i,j]) < eps:
                matrix[i,j] = 0
    print(matrix)
        
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
    matrix[0:len(matrix),0:len(matrix)] = I - matrix[0:len(matrix),0:len(matrix)] 
            
def result(matrix):
    #giải nghiệm và ỉn ra kết quả

    kq = []
    for i in range(len(matrix)):
        x = matrix[i,len(matrix)]/matrix[i,i]
        kq.append(x)
    print("Nghiệm của hệ phương trình là: \n", kq)

# main--------------------------------------------------------------------------------------
if __name__ == "__main__":
    matrix = np.loadtxt("data.txt")
    addIdentityMat(matrix)
    gaussJordan(matrix)
    result(matrix)

