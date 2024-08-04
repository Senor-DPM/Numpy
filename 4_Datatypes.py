import numpy as np

# Like Python, NumPy has it's own data types for its arrays. These include :
'''
integer - i
boolean - b
unsigned integer - u
float - f
complex - c
timedelta - m
datetime - M
object - O
string - S
unicode string - U
void - V
'''

# To check the data type of an array, we can use the dtype method.
arr1 = np.array([1,2,3])
arr2 = np.array(['books','pens','pencils'])
print(arr1.dtype)
print(arr2.dtype)

# To create an array of acertain data type, we can use the dtype attribute.
arr3 = np.array([1,2,3], dtype = "S")
print(arr3)
print(arr3.dtype)
# Keep in mind that some data types may cause an error for certain values, like entering "a" in an array with dtype = "i".

# To convert an existing array's data type, you can use the astype() method. It will return an array with the converted data type.
oldArr = np.array([1.1, 5.7, 3.6])
newArr = oldArr.astype('i')
print(newArr)
print(newArr.dtype)