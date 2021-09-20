from tkinter import *
root=Tk()
def rightclick(event):
    print("right click is pressed")

def leftclick(event):
    print("left click is pressed")

def middleclick(event):
    print("middle click is pressed")

btn=Button(root,text="Right click",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"))
btn.bind("<Button-3>",rightclick)
btn.pack()

btn1=Button(root,text="middle click",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"))
btn1.bind("<Button-2>",middleclick)
btn1.pack()

btn2=Button(root,text="left click",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"))
btn2.bind("<Button-1>",leftclick)
btn2.pack()
root.wm_iconbitmap('calci.ico')
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()