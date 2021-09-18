from tkinter import *
root=Tk()
def get_data():
    print(s.get())
    s.set('')

l=Label(root,text="Enter Your name",bg="yellow", fg="red",
        font=("Comic Sans Ms", 15, "bold"))
l.grid(row=0,column=0)
s=StringVar()
text1=Entry(root,font=("Comic Sans Ms", 15, "bold"),textvariable=s)
text1.grid(row=0,column=1)
btn=Button(root,text="Click        Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.grid(row=1,column=0)
#root.geometry("600x400+250+100")
#root.resizable(0,0)
mainloop()