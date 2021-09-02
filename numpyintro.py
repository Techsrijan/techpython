#import numpy
from numpy import *

arr=array([4,5,6,7])
print(arr)
print(arr.dtype)

'''
There are six ways to create an array using numpy
1.array()
2.linspace
3.logspace
4.arange
5.zeros
6.ones
'''

arr1=linspace(1,15,15)
print(arr1)

arr2=logspace(1,50)  # by default 50
print(arr2)

arr3=arange(1,15,6)
print(arr3)

arr5=zeros(10)
print(arr5)

arr6=ones(10,int)
print(arr6)