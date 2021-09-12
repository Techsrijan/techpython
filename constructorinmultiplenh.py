class A:
    def __init__(self):
        print("class A constructor")

class B:
    def __init__(self):
          print("class B constructor")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("class C constructor")

c=C()