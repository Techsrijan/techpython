from turtle import *
t=Turtle()
w=Screen()
w.title("Control Turtle")
def star():
    t.forward(200)
    t.left(216)
def up():
    t.left(90)
    t.forward(100)

def down():
    t.backward(100)

def left():
    t.left(90)

def right():
    t.forward(100)

def st():
    for i in range(5):
        star()

t.write("Use Up down left and right arrow key",font=("Comic Sans Ms",12,"normal"))
#w.onkey(up,'Up')
w.onkey(up,"D")
w.onkey(down,'Down')
w.onkey(left,'Left')
w.onkey(right,'Right')
w.onkey(st,"s")

w.listen()

done()