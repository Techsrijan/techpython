from tkinter import *
root=Tk()
def get_data():
    print(s.get())
    s.set('')

l=Label(root,text="Enter Your name",bg="yellow", fg="red",
        font=("Comic Sans Ms", 15, "bold"))
l.place(x=50,y=30)
s=StringVar()
text1=Entry(root,font=("Comic Sans Ms", 15, "bold"),textvariable=s)
text1.place(x=300,y=30)
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.place(x=160,y=100)
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()