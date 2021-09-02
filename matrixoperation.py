from numpy import *
arr=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]

])

arr2=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]

])

arr3=arr+arr2
print(arr3)

# matrix multiplication
arr5=arr@arr2
print(arr5)

arr6=dot(arr,arr2)
print(arr6)