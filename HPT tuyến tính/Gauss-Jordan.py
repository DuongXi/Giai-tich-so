import numpy as np

def JGaussThuan(matrix):
    count = -1.0
    index = []
    left = []
    for c in range(0, len(matrix)):
        left.append(c)
    for c in range(0,2):
        for i in range(0, len(matrix)):
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
    print(count)
    for j in range(0,len(matrix)):
        if j == count:
            pass
        else:
            matrix[j] = matrix[j] - (matrix[j,count]/matrix[count,count])*matrix[count]
    print(matrix)
            
def JGaussNghich(matrix):
    for i in range(len(matrix)):
        x = matrix[i,len(matrix)]/matrix[i,i]
        kq.append(x)

# main--------------------------------------------------------------------------------------
file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
kq = []
# print(max(np.diag(abs(matrix))))
JGaussThuan(matrix)
JGaussNghich(matrix)
# print(matrix)
print(kq)