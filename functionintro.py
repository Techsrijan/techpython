from math import *
def msg():  #function definition
    print("good morning")

msg()  # function call

msg()



def test():
    print("funtion concept cleard")
    print("thank you")

test()
msg()
test()

def add():
    a,b=4,5
    c=a+b
    print("Sum=",c)

add()

def add1(x,y):
    c=x+y
    print('Add=',c)

add1(4,10)

'''
void add1(int x,int y)
{
int c;
c=x+y;
printf("%d",c)
}
'''

a=int(input("Enter First Number"))
b=int(input("enter Second Number"))
add1(a,b)

print(sqrt(36))

print(sqrt(a))

#sqrt(50)

def testadd(p,q):
    d=p+q
    return d

f=testadd(5.0,66)
print(f)

print(testadd(5,8))

def morereturn(g,t):
    a=g+t
    b=g-t
    return g,t

s,t=morereturn(95,88)
print(s,t)