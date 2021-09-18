from tkinter import *
root=Tk()
def msg():
    print("Hello Tkinter")

def table():
    i = 1
    while i <= 10:
        print(2, "*", i, "=", 2 * i)
        i = i + 1

root.title("My App")
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",15,"bold"),command=msg)
btn.pack(side=TOP)

btn1=Button(root,text="Table Print",bg="yellow",fg="red",
           font=("Comic Sans Ms",15,"bold"),command=table)
btn1.pack(side=BOTTOM)

root.geometry("300x400+250+100")
root.resizable(0,0)
mainloop()