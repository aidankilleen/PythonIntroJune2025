# numpy_investigation.py


import numpy as np


lst = [1, 2, 3]
print (lst)

#lst1 = [1,2,3]
#1lst = [1,2,3]

arr = np.array([1,2,3])

print (arr)

result = arr * 2

print (result)

# creation functions

zeros = np.zeros((3,3))
print (zeros)

ones = np.ones((3,3))
print (ones)

sequence = np.arange(0, 10, 2)
print(sequence)

sequence = np.linspace(0, 1, 15)
print (sequence)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print (arr)

arr = arr.reshape((2, 6))

print (arr)

arr = arr.reshape((1, 12))

print (arr)

# slicing 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print (arr)

el = arr[2, 2]
print (el)

col = arr[:, 1]
print (col)

subset = arr[0:2, 0:2]
print (subset)



















