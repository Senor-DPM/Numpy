import numpy as np

arr1 = np.array([1,2,3,4,5])

# Indexing in arrays are similar to that of lists in Python, with the first element's index being 0.

print(arr1[0]) # First elements from the left.
print(arr1[-2]) # Second element from the right.

# If arrays are multidimensional, we can access inner elements using commas.

arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[1,2]) # Third element of the second array.

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3[1,0,2]) # Second element of the first nested array of the second array.