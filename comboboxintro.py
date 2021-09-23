from tkinter import *
from tkinter import ttk


root=Tk()
def get_data():
    x=c.get()
    print(x)
#l=['UP','BIHAR',"MP","DELHI","ASAM"]
l=list(range(1,31))
c=ttk.Combobox(root,values=l)
c.set('Select Your state')
c.pack()

btn=Button(root,text="get combo data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.place(x=160,y=100)
root.geometry("800x400+250+100")
root.resizable(0,0)
mainloop()