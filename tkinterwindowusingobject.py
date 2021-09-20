from tkinter import *
class MyWindow:
    def msg(self):
        print("hi")

    def __init__(self,master):
        self.btn=Button(master,text="click me",command=self.msg)
        self.btn.pack()


root=Tk()
win=MyWindow(root)
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()
