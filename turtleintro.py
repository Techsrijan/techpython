from turtle import *
t=Turtle()
w=Screen()
#w.bgcolor("grey")
#w.bgpic('test.gif')
w.title("                               My turtle")
#t.pencolor("red")

t.pensize(10)
t.shape('turtle')
t.hideturtle()
t.speed(1)
def sq():
    for i in range(4):
        t.forward(100)
        t.left(90)
t.color("red","#1877f2")
t.begin_fill()
sq()
t.end_fill()
t.right(90)
t.penup()
t.fd(100)
t.pendown()
t.pencolor("green")
sq()
'''
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

for i in range(4):
    t.forward(100)
    t.left(90)
'''
done()