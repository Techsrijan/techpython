from tkinter import *
from tkinter import filedialog,colorchooser
root=Tk()
def msg(event=''):
    print(text.get(1.0,END))

def selecteddata():
    s=text.selection_get()
    print(s)
    pos=text.search(s,1.0,stopindex=END)
    print(pos)

def cleardata():
    text.delete(1.0,END)

global result
def openfile():
     result=filedialog.askopenfile(initialdir="/",title="Open file",
                                   filetypes=(("Text File","*.txt"),("All File","*.*")))
     print(result)
     for data in result:
         print(data)
         text.insert(INSERT,data)


def savefile():
    f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    print(f)
    s=text.get(1.0,END)
    f.write(s)

def changefont():
    clr=colorchooser.askcolor(title="Select font Color")
    print(clr)
    text.configure(foreground=clr[1])

def changeback():
    clr = colorchooser.askcolor(title="Select background Color")
    print(clr)
    text.configure(background=clr[1])

root.bind("<Control-y>",msg)

text=Text(root,width=50,height=5,wrap=WORD,padx=2,pady=5,
          font=("Comic Sans Ms",12,"bold"),selectbackground="red")
text.insert(INSERT,"Welcome to this window")
text.pack()
btn=Button(root,text="Get Text data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=msg)

btn.pack()

btn1=Button(root,text="Get Selected Text data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=selecteddata)

btn1.pack()


btn2=Button(root,text="Clear Text data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=cleardata)

btn2.pack()


btn3=Button(root,text="Save file",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=savefile)

btn3.pack()


btn4=Button(root,text="Open file",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=openfile)

btn4.pack()

btn5=Button(root,text="change font color",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=changefont)

btn5.pack()

btn6=Button(root,text="change bachgound color",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=changeback)

btn6.pack()


#root.geometry("600x400+250+100")
#root.resizable(0,0)
mainloop()