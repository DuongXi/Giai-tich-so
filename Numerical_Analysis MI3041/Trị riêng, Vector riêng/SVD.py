import numpy as np
from Danielevsky import *
import math

# def SVD(matrix):
#     rank = np.linalg.matrix_rank(matrix)
#     n = len(matrix)
#     U = []
#     V = []
#     sigma = np.eye(n)
#     # lamda , v = Danielevsky(a)
#     for i in range(n):
#         v_ = v[i].reshape(-1,1)/np.linalg.norm(v[i])
#         V.append(v_)
#     for i in range(n):
#         sigma[i,i] = math.sqrt(lamda[i])
#     if rank == n:
#         pass
#     for i in range(n):
#         U.append(A@V[1]/sigma[i,i])
#     return U, sigma, V

def addIdentityMat(matrix):
    #Thực hiện khi đề bài cho dạng (A+aI)X=b
    a = float(input("Hệ số ma trận đơn vị "))
    I = np.eye(len(matrix))
    matrix[0:len(matrix),0:len(matrix)] = matrix[0:len(matrix),0:len(matrix)]  + a*I

#main-----------------------------------------------------------------------
A = np.loadtxt("data1.txt")
# AT = np.transpose(A)
# n = len(A)
# # print(AT)
# a = (AT @ A)
# print(a)


# FindSigma(lamda)
# FindV(v)
# print("Ma trận Sigma: \n",Sigma)
u, sigma, v = np.linalg.svd(A)
# u, sigma, v = SVD(A)
print(u)
print(sigma)
print(v)
# addIdentityMat(A)