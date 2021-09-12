'''
constructor is a special member function which will run
automatically when the object is created
'''

class Test:
    def msg(self):
        print('I will run with the help of object and . operator')

    #constructor
    def __init__(self):
        print("i will run automatically when the object is created")


t=Test()  # creating object
t.msg()
t2=Test()