from turtle import *
win=Screen()
win.bgcolor("black")
color=["red","orange","yellow","grey","blue"]
t=Turtle()
for k in range(50):
    t.color(color[k%5])
    t.forward(k)
    t.speed(0)
    t.circle(80)
    t.left(90)

done()