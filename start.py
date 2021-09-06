from turtle import *
t=Turtle()
l=["red","blue","green","yellow","pink"]

def star():
    t.forward(200)
    t.left(216)

for i in range(5):
    t.pencolor(l[i])
    star()
done()