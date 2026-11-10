import numpy as np

# Create two matrices
A = np.array([
    [2, 1],
    [1, 1]
])

B = np.array([
    [3, 2],
    [4, 5]
])

# 1. Matrix Multiplication
C = A @ B

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Multiplication (A x B):")
print(C)

# 2. Matrix Inversion
A_inv = np.linalg.inv(A)

print("\nInverse of Matrix A:")
print(A_inv)

# 3. Verify the inverse
result = A @ A_inv

print("\nVerification (A x A_inverse):")
print(np.round(result, 10))
