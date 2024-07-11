import numpy as np

def gauss_jordan_elimination(A, B):
    m, n = A.shape
    p = B.shape[1]
    
    # Tạo ma trận mở rộng bằng cách ghép A và B
    M = np.hstack([A, B])
    
    # Khử Gauss-Jordan
    for i in range(min(m, n)):
        # Tìm hàng với phần tử đầu tiên lớn nhất
        max_row = max(range(i, m), key=lambda r: abs(M[r, i]))
        M[[i, max_row]] = M[[max_row, i]]
        
        # Đảm bảo phần tử chéo không phải là 0
        if abs(M[i, i]) < 1e-10:
            raise ValueError("Ma trận A có thể không có hạng đầy đủ")
        
        # Chia hàng hiện tại để phần tử chính là 1
        M[i, i:] /= M[i, i]
        
        # Loại bỏ các phần tử khác trong cột i
        for j in range(m):
            if j != i:
                ratio = M[j, i]
                M[j, i:] -= ratio * M[i, i:]
    print(M)
    # Nghiệm là phần mở rộng của ma trận đơn vị
    X = M[:, n:]
    
    return X

# Giả sử ma trận A và B
A = np.loadtxt("data.txt")
B = np.loadtxt("data1.txt")


# Giải hệ phương trình
X = gauss_jordan_elimination(A, B)

print("Ma trận nghiệm X:")
print(X)
