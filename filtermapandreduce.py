from functools import *
num=[5,6,77,88,4,5,66,79,85,2]

even=list(filter(lambda n:n%2==0,num))
print(even)

data=list(map(lambda n:n+5,even))
print(data)

result=reduce(lambda a,b:a+b,data)
print(result)