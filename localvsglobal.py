x=5 #global variable
y=50
def test():
    y=10  #local variable
    global w
    w=20
    a=globals()['y']
    print("Global y=",a) #50
    print("Y=",y)  #10

test()
#print("Y=",y)
print("X=",x)
print("W=",w)
