from tkinter import *
from PIL import Image,ImageTk
import time
root=Tk()
root.title("Text Slider")
play_image=ImageTk.PhotoImage(Image.open('images/playButton.png'))
pause_image=ImageTk.PhotoImage(Image.open('images/stopButton.png'))
count=0
slider_text=''
run=0
def msg():
    slider()
def slider():
    global slider_text,count,run
    text=[play_image,pause_image,play_image]

    if count>=len(text):
        count=0
        slider_text=''
    slider_text=text[count]
    count=count+1
    #run=run+1
    btn.configure(image=slider_text)
    btn.after(500, slider)
    '''
    if run<=2:
        btn.after(100,slider)
    if run==3:
        run=0
    '''

btn=Button(root,font=("Comic Sans MS",18),
            fg="red", image=play_image,command=msg)
btn.pack()

root.geometry("800x500+150+120")
root.mainloop()
