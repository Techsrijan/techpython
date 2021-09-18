from tkinter import *
root=Tk()
def get_data():
    #print(s.get())
    a=s.get()
    c.set(a)
    s.set('')

l=Label(root,text="Enter Your name",bg="yellow", fg="red",
        font=("Comic Sans Ms", 15, "bold"))
l.place(x=50,y=30)
s=StringVar()
text1=Entry(root,font=("Comic Sans Ms", 15, "bold"),justify="right",bd="15",textvariable=s)
text1.place(x=300,y=30)

c=StringVar()
result=Label(root,fg="red",
        font=("Comic Sans Ms", 15, "bold"),textvariable=c)
result.place(x=160,y=200)

btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.place(x=160,y=100)


root.geometry("800x400+250+100")
root.resizable(0,0)
mainloop()