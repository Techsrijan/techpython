from tkinter import *
root=Tk()
canvas=Canvas(root,width=500,height=400,bg="yellow")
line=canvas.create_line(100,100,300,400,width=5,fill="red")
rec=canvas.create_rectangle(100,100,300,300,fill="blue",outline="white",width="4")
cir=canvas.create_oval(100,100,200,300,fill="red",outline="white",width=5)
arc=canvas.create_arc(100,100,300,300,fill="yellow",outline="white",extent=60)
point=[200,110,480,200,280,280,200,110]
poly=canvas.create_polygon(point,fill="green")
canvas.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()