from tkinter import *
from tkinter import simpledialog
root=Tk()
def get_data():
    print(i.get())
    print(j.get())
    if i.get()==1:
        print("HINDI")
    if j.get()==1:
        print("ENGLISH")
f=LabelFrame(root,text="Select Your Language Known")
i=IntVar()
j=IntVar()
radio=Checkbutton(f,text="Hindi",variable=i)
radio.pack()
radio1=Checkbutton(f,text="English",variable=j)
radio1.pack()
f.pack()



btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()