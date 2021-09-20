from tkinter import *
root=Tk()
def msg(event=''):
    print("hi")
main_menu=Menu(root)
#root.config(bg="red")
root.config(menu=main_menu)
root.bind("<Control-n>",msg)
#creating file menu
file_menu=Menu(main_menu,tearoff=0)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="NEW",accelerator="Ctrl+N",command=msg)
file_menu.add_separator()
file_menu.add_command(label="OPEN",accelerator="Ctrl+O")

# creating submenu
save_menu=Menu(file_menu,tearoff=0)
save_menu.add_command(label="save as",accelerator="Ctrl+O")

file_menu.add_cascade(label="SAVE",menu=save_menu)


#creating edit menu
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=edit_menu)
edit_menu.add_command(label="CUT")
root.geometry("600x400+250+100")
root.resizable(0,0)
mainloop()