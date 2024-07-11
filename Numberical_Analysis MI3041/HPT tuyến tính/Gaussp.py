import numpy as np

def gaussian_elimination(A, B):
    m, n = A.shape
    p = B.shape[1]
    
    # Tạo ma trận mở rộng bằng cách ghép A và B
    M = np.hstack([A, B])
    
    # Khử Gauss
    for i in range(min(m, n)):
        # Tìm hàng với phần tử đầu tiên lớn nhất
        max_row = max(range(i, m), key=lambda r: abs(M[r, i]))
        M[[i, max_row]] = M[[max_row, i]]
        
        # Đảm bảo phần tử chéo không phải là 0
        if abs(M[i, i]) < 1e-10:
            raise ValueError("Ma trận A có thể không có hạng đầy đủ")
        
        # Loại bỏ các phần tử dưới hàng hiện tại
        for j in range(i + 1, m):
            ratio = M[j, i] / M[i, i]
            M[j, i:] -= ratio * M[i, i:]
    print(M)
    # Giải ngược
    X = np.zeros((n, p))
    for k in range(p):
        for i in range(n-1, -1, -1):
            if i < m:
                X[i, k] = (M[i, n+k] - np.dot(M[i, i+1:n], X[i+1:, k])) / M[i, i]
            else:
                X[i, k] = 0
    
    return X

# Giả sử ma trận A và B
A = np.loadtxt("data.txt")
B = np.loadtxt("data1.txt")

# Giải hệ phương trình
X = gaussian_elimination(A, B)

print("Ma trận nghiệm X:")
print(X)
