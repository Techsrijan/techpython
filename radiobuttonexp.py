from tkinter import *
from tkinter import simpledialog
from PIL import Image,ImageTk
root=Tk()

play_image=ImageTk.PhotoImage(Image.open('images/playButton.png'))
#pause_image=ImageTk.PhotoImage(Image.open('images/stopButton.png'))
def get_data():
    print(i.get())
    print(j.get())
    if i.get()==1:
        print("MALE")
    elif i.get()==2:
        print("FEMALE")
f=LabelFrame(root,text="Select Your Gender")
i=IntVar()
radio=Radiobutton(f,text="MALE",value=1,variable=i)
radio.pack()
radio1=Radiobutton(f,text="FEMALE",value=2,variable=i)
radio1.pack()
f.pack()


j=IntVar()
radio3=Radiobutton(root,text="JAVA",value=1,variable=j)
radio3.pack()
radio4=Radiobutton(root,text="PYTHON",value=2,variable=j)
radio4.pack()
btn=Button(root,image=play_image,bd="0",command=get_data)
btn.pack()
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()