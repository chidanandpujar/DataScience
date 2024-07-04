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


