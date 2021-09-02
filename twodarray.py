from numpy import *
arr=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]

])

print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)

# converting 2 d arrray into 1-d array
arr2=arr.flatten()
print(arr2)

arr3=array([
    [1,2,3,4,5,6],
    [4,5,6,1,2,3]
])
print(arr3.shape)

print(arr3.reshape(3,4))
print(arr3.ndim)

arr5=arr3.reshape(2,2,3)
print(arr5.ndim)
print(arr5)
