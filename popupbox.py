from tkinter import *
from tkinter import simpledialog
root=Tk()
def get_data():
    sum=0
    for i in range(5):
        s = simpledialog.askinteger("MARKS INPUT BOX ", "Enter Your Marks")
        sum=sum+s
        print(s)
    print(sum)


btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()