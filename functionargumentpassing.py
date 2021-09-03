def person(name,age):
    print("Name=",name)
    age=age+10
    print("Age=",age)

person("Ashwani",35)

#person(25,'ram')

'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument 
4. keyword variable length argument 
'''

person(name='rohan',age=5)

person(age=55,name='mohan')

def add1(x,y,z):
    c=x+y+z
    print('Add=',c)

add1(3,5,5)

def add(x,*y):
    print(x)
    print(y)
    sum=x
    for i in y:
        sum=sum+i
    print(sum)

add(4,1,2,3,4,5)


def add1(*y):
    print(y)
    sum=0
    for i in y:
        sum=sum+i
    print(sum)

add1(4,1,2,3,4,5)

def persondata(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

persondata(name='ram',age=44,mobile=99956477677,gender='m',city='gkp')