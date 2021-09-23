from tkinter import *
root=Tk()
def get_data():
    selecteditem = l.curselection()
    print(selecteditem)
    for item in selecteditem:
        print(l.get(item))

def deletedata():
    selecteditem = l.curselection()
    for item in selecteditem:
        print(l.delete(item))
frame=Frame(root)
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(frame,yscrollcommand=scroll.set,selectmode=SINGLE)
l.pack()
for i in range(1,100):
    l.insert(END,i)
scroll.config(command=l.yview)
frame.pack()
btn=Button(root,text="get list data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.place(x=160,y=100)

btndelete=Button(root,text="deleteitem",fg="white",bg="red",bd=10,font=("Times", "12", "bold"),command=deletedata)
btn.pack()
btndelete.pack()
root.geometry("800x400+250+100")
root.resizable(0,0)
mainloop()