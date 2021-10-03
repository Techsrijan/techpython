from turtle import *
import time
t=Turtle()
t.shape('turtle')
t.color('black','orange')
t.penup()
t.goto(30,30)
s=10
for i in range(50):
    s=s+2
    t.stamp()
    t.forward(s)
    t.right(25)
    time.sleep(0.5)

done()