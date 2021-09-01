'''
array is collection of similar data type.
'''
#import array
from array import *
import time

marks=array('f',[4,5,6,7,8,9,8.7])
print(marks)

print(len(marks))

print(marks[4])
print(marks.buffer_info())

print(marks.typecode)

for i in marks:
    print(i)

for i in range(len(marks)):
    print(marks[i])
    time.sleep(1)


print(sum(marks))
print(min(marks))
