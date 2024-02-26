# NumPy exercises 
import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1
a

# b. Create a vector with values ranging from 10 to 49 
b = np.arange(10, 49)
b

# c. Reverse a vector (first element becomes last)
c = np.array([1,2,3,4,5])
c = a[::-1] 
c

# d. Create a 3x3 matrix with values ranging from 0 to 8 
d = np.array([[0,1,2],[3,4,5],[6,7,8]])
d

# e. Find indices of non-zero elements from [1,2,0,0,4,0] 
e = np.array([1,2,0,0,4,0])
e2 = e != 0
e[e2]

# f. Create a random vector of size 30 and find the mean value 
f = np.random.random([30])
fMean = np.mean(f)

# g. Create a 2d array with 1 on the border and 0 inside 
g = np.array([[1,1,1], [1,0,1], [1,1,1]])
g

# h. Create a 8x8 matrix and fill it with a checkerboard pattern
h = np.zeros([8,8])
# Put 1 where both row and column are even or odd 
for i in range(8):
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            h[i,j] = 1
h

# i. Create a checkerboard 8x8 matrix using the tile function 
i = np.array([1,0])
i = np.tile(i, (8,4))
# Flip the odd rows 
for row in range(8):
    if row % 2 == 1:
        i[row,] = i[row,][::-1]
i

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
j = np.arange(11)
j2 = (j < 3) | (j > 8)
j[j2]

# k. Create a random vector of size 10 and sort it 
k = np.random.random(10)
k_sorted = np.sort(k)
k_sorted

# l. Consider two random array A anb B, check if they are equal 
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)
equal

# m. How to calculate the square of every number in an array in place 
#    (without creating temporaries)?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.sqrt(Z)
print(Z.dtype)
















