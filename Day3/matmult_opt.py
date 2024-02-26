# Program to multiply two matrices using NumPy's dot product functions 
import numpy as np

N = 250

# NxN matrices
X = np.random.randint(0,100,size=(N,N))
Y = np.random.randint(0,100,size=(N,N+1))

# Calculate dot product 
result = np.dot(X,Y)

# Print result 
for r in result:
    print(r)