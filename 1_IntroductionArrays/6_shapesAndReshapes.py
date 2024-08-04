import numpy as np

# The shape of an array is the number of elements it contains.
# We can find the shape of an array using the shape attribute.
# This returns a tuple of elements signifying the shape of each dimension of an array.
arr1 = np.array([1,2,3,4,5,6]) # 1D Array
print(arr1.shape)

# In the case of a 2D array, it will return a tuple with 2 element, each signifying the size of each dimension.
# Outer dimension's shape is to the left of the inner dimension's shape.
arr2 = np.array([[1,2,3,4],[5,6,7,8]]) # 2D Array
print(arr2.shape)

# We can also reshape arrays. This can add/remove dimension or change the number of elements in each dimension.
# To reshape an array, use the reshape() method.
# This returns a view of the original array with the newly assigned shape.
newArr1 = arr1.reshape(2,3)
newArr2 = arr2.reshape(1,8)
print(newArr1)
print(newArr2)
# Note : Some reshapes aren't possible depending on the array.
# For eg. you cannot reshape arr2 to (3,3) as we require 9 elements in the array for that..

# You are allowed to have one unknown dimension (denoted by -1). Python will calculate the unknown dimension by itself.
newArr3 = arr2.reshape(4,-1)
print(newArr3)

# To convert any multi-dimensional array to 1D, just reshape the array to -1. This is called Flattening an Array.
flatArr = arr2.reshape(-1)
print(flatArr)