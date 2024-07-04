import numpy as np
# To create matrix of 2X2
A = np.array[(1,2), (3,4])
print(A)

# To create an Identity matrix of 2x2
B = np.identity(2)
print(B)

# To create matrix of random numbers 
C = np.random.randn(2)
print(C)

# To multiply matrices
D = np.random.randn(4,3)
E = np.random.randn(3,4)
print(np.shape(D))
print(np.shape(E))

print(D.dot(E))
print(np.dot(D, E))
print('=============')
print(E.dot(D))
print(np.dot(E, D))

#Inverse of a matrix
F = np.random.randn(3,3)
F_inverse = np.linalg.inv(F)
print(F_inverse)

# dot product of matrix and its inverse of matrix is same
print(F.dot(F_inverse))
print(F_inverse.dot(F))

#Transpose of a matrix
A = np.arange(6).reshape((3,2))
B = np.arange(8).reshape((2,4))
print(A)
print(A.T)

# (AB)T = BT AT

# Extract values from matrices/arrays
A = np.array[(0,1), (2,3), (4,5)]
print(A)

print(A[:,1] > 4)
print(np.argmax(A[:,1] >4))
print(A[A[:,1] >4])



