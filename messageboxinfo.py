from tkinter import *
from tkinter import messagebox
root=Tk()
def get_data():
    #res=messagebox.askyesno("Question Box","Do you like coffee?")
    res=messagebox.showwarning()
    print(res)
    if res==True:
        print("Give me 10 Rs")

btn=Button(root,text="Click        Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.pack()

root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()