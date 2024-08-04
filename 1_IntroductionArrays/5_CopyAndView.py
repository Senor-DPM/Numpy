import numpy as np

arr1 = np.array([1,2,3,4,5])

# Copy and View work similarly to "Shallow Copy" and "Deep Copy" of Python with a couple differences

# Creating a copy of an array makes an entirely new array.
cArr = arr1.copy()

# Creating a view of an array just assigns that same array to another variable (like a=b).
vArr = arr1.view()

# Changes in the main array will reflect on the view, but not on the copy.
arr1[2] = 99
print(cArr)
print(vArr)

# A copy owns its data, whereas a view only shows another array's data.
# The "base" attribute returns None if an array owns it's data, otherwise it will print the base array's data.
print(cArr.base)
print(vArr.base)