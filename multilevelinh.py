class A:
    def msg(self):
        print("class A")

class B(A):
    def msg1(self):
        print("class B")

class C(B):
    def msg2(self):
        print("class C")

t=C()
t.msg()
t.msg1()
t.msg2()