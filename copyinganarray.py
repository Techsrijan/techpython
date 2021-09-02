from numpy import *
arr=array([4,5,6,7])
print(arr,id(arr))

# aliasing
arr2=arr
print(arr2,id(arr2))

arr[0]=4000
print(arr,id(arr))
print(arr2,id(arr2))

# what if u want two different address

arr3=array([4,88,99,22])
# shallow copy
arr4=arr3.view()
print(arr3,id(arr3))
print(arr4,id(arr4))
arr3[2]=333
print(arr3,id(arr3))
print(arr4,id(arr4))


# what if u want two different address and change in one does not affect
#another
arr5=array([4,88,99,22])
# Deep copy
arr6=arr5.copy()
print(arr5,id(arr5))
print(arr6,id(arr6))
arr5[2]=333
print(arr5,id(arr5))
print(arr6,id(arr6))