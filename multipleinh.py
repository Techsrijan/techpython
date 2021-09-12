class Theory:
    def the_marks(self):
        print("theory Marks")

class Sessional:
    def sess_marks(self):
        print("Sessional Marks")

class result(Theory,Sessional):
    def res(self):
        print("Result")

t=result()
t.the_marks()
t.sess_marks()
t.res()