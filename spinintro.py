from tkinter import *
from tkinter import ttk
root=Tk()
def get_data():
     print(s.get())

def get_scaledata():
    print(sc.get())

sc=Scale(root,from_=0,to=15,orient=HORIZONTAL,length=200,width=10,sliderlength=50)
sc.set(5)
sc.pack()

frame=LabelFrame(root,text="Spin Data",padx=10,pady=20)
s=Spinbox(frame,from_=1,to=12)
s.pack()

btn=Button(frame,text="get spin data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.pack()

btn=Button(root,text="get scale data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_scaledata)
btn.pack()
frame.pack()
root.geometry("800x400+250+100")
root.resizable(0,0)
mainloop()