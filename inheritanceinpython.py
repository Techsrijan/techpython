'''
Deriving a new class from the base class is known as inheritance.
types of inheritance
1. single level inheritance
2. multilevel inheritance
3. hierarchical inheritance
4. multiple inheritance
5. hybrib inheritance
'''

class Room:   #parent class   base class
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class GuestRoom(Room):   # child class   derived class
    def msg(self):
        print("guest Room")

'''
r=Room()
r.area(5,4)
'''
g=GuestRoom()
g.msg()
g.area(4,9)