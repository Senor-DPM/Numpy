import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])

# Slicing an array works exactly as slicing a list in Python.
print(arr1[0:4]) # Prints elements from 0 to 3
print(arr1[5:8]) # Prints elements from 5 to 8
print(arr1[-5:-1]) # Prints elements from -5 to -1
print(arr1[0:7:2]) # Prints elements from 0 to 6 with step 2
print(arr1[-2:-9:-1]) # Prints elements from -9 to -2 (backwards)

# Slicing 2D Arrays works the same using commas, but here are some key points :
# i) Slicing only one dimension will return a 1D Array.
# ii) Slicing both dimensions will return a 2D Array.

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1, 2:4]) # Returns a 1D array
print(arr2[0:2, 3]) # Returns a 1D array
print(arr2[0:2,1:4]) # Returns a 2D array