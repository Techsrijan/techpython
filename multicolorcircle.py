from turtle import *
t=Turtle()
l=["red","blue","green","yellow","pink"]
#t.up()
#t.goto(200,0)
'''for i in range(5):
    t.down()
    t.color(l[i])
    t.pensize(20)
    t.circle(100)
    t.up()
    t.backward(150)

for i in range(5):
    t.down()
    t.begin_fill()
    t.fillcolor(l[i])
    t.circle(100)
    t.end_fill()
    t.up()
    t.backward(100)
    
'''
for i in range(150):
    t.color(l[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(58)
done()