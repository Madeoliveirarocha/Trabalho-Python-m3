import time
import random
import numpy as np

def multiply_matrices(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                soma += A[i][k] * B[k][j]
            result[i][j] = soma
    return result

N = 300  # 10.000 é impossível

A = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]
B = [[random.randint(1, 10) for _ in range(N)] for _ in range(N)]

start = time.time()
resultado_puro = multiply_matrices(A, B)
end = time.time()
print(f"Tempo com Python puro: {end - start:.2f} s")

A_np = np.array(A)
B_np = np.array(B)

start = time.time()
resultado_numpy = np.matmul(A_np, B_np)
end = time.time()
print(f"Tempo com NumPy: {end - start:.4f} s")
