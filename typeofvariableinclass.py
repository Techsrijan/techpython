'''
there are two type of variable in a class
1. instance variable --varibale declared inside function
2. class variable
'''

class Car:
    wheel=4   # class variable
    def __init__(self):  #deafult
        self.mil=25
        self.compnay="maruti"

    def print_wheel(self):
        print(self.wheel)

c1=Car()
c2=Car()
print(c1.mil,c1.compnay,c1.wheel)
#c1.mil=50
Car.mil=800
Car.wheel=6
print(c1.mil,c1.compnay,c1.wheel)
print(c2.mil,c2.compnay,c2.wheel)

c1.print_wheel()