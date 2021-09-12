class Student:
    def student_info(self):
        print("Ram",55)


t=Student()   # t is object
Student.student_info(t)

t.student_info()
t2=Student()
t2.student_info()