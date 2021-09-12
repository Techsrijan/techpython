'''
there are 3 types of method
1. instance method--by defalut argument self
2. class method
3. static method
'''

class Student:
    school="techsrijan"
    def __init__(self,m1,m2,m3):  #parametrized
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return ((self.m1+self.m2+self.m3)//3)

    @staticmethod   # decorator
    def msg():
        print("this is static method")

    @classmethod
    def scholl_name(cls):
        return cls.school

s1=Student(50,20,30)
print("avg marks=",s1.avg())
Student.msg()
print(Student.scholl_name())
