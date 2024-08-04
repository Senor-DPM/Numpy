import numpy as np

# To create an array, simply use the array() method on a list or tuple. It's class is "numpy.ndarray".

arrL = np.array([1,2,3,4,5])
print(arrL, "\n", type(arrL), "\n")
arrT = np.array((1,2,3,4,5))
print(arrT, "\n", type(arrT), "\n")

# Dimensions of an array can be defined as the levels of depth (nested arrays).
# Each element of an array is a 0D array.

arr1 = np.array([1,2,3,4,5]) # 1D Array
arr2 = np.array([[1,2,3],[4,5,6]]) # 2D Array
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr1, arr2, arr3, sep = "\n\n")

# To check the dimensions of an array, you can use the ndim method.

print(arr1.ndim, arr2.ndim, arr3.ndim)

# To create an n-dimension array, you can use the ndmin attribute.

arr4 = np.array([1, 2, 3, 4], ndmin = 5) # Creates a 5D array
print(arr4)
print("No. of Dimension = ", arr4.ndim)