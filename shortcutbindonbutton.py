from tkinter import *
root=Tk()
def msg(event=''):
    print("good morning")

root.bind("<Control-y>",msg)
btn=Button(root,text="Right click",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=msg)

btn.pack()
root.wm_iconbitmap('calci.ico')
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()