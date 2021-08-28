#import math
#import math as m
from math import *
a=int(input("Enter First side of traingle"))
b=int(input("enter Second side of traingle"))
c=int(input("enter Third side of traingle"))
print("a=",a,"b=",b,"C=",c)
s=(a+b+c)/2
#area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#area=m.sqrt(s*(s-a)*(s-b)*(s-c))
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area of traingle=",area)