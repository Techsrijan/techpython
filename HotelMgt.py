from tkinter import *
from tkinter import messagebox
import pymysql

taz=Tk()
width=taz.winfo_screenwidth()
#print(width)
height=taz.winfo_screenheight()
#print(height)
taz.title("Hotel Managment System")

##################### add item window ####################
def addItemWindow():
    remove_all_widgets()
    mainheading()

################ logout process #############################
def logout():
    remove_all_widgets()
    mainheading()
    loginwindow()
############ to clear all widgets on the screen #################
def remove_all_widgets():
    global taz
    for widget in taz.winfo_children():
        widget.grid_remove()
########## welcome window ################################
def welcomewindow():
    remove_all_widgets()
    mainheading()
    loginLabel = Label(taz, text="Welcome user", font="Arial 30")
    loginLabel.grid(row=1, column=1, columnspan=2, pady=10)

    logoutButton = Button(taz, text="Logout", width=20, height=2, fg="green", bd=10, command=logout)
    logoutButton.grid(row=2, column=1, columnspan=2)

    logoutButton = Button(taz, text="Manage Hotel", width=20, height=2, fg="green", bd=10, command=addItemWindow)
    logoutButton.grid(row=3, column=1, columnspan=2)

    logoutButton = Button(taz, text="Bill Generation", width=20, height=2, fg="green", bd=10)
    logoutButton.grid(row=4, column=1, columnspan=2)

###############database connect######################################
def dbconfig():
    global mycursor,conn
    conn=pymysql.connect(host="localhost",user="root",db="hoteltaz")
    mycursor=conn.cursor()

################ login process ##########
def adminlogin():
    a=usernameVar.get()
    b=passwordVar.get()
    if a=='' or b=='':
        messagebox.showwarning("Login Check Window", "Please Enter User Name and Password")
        usernameVar.set("")
        passwordVar.set("")
    else:
        dbconfig()
        que = "select * from login_info where binary userid=%s and binary password=%s"
        val = (a, b)
        mycursor.execute(que, val)
        flag=False
        data = mycursor.fetchall()
        for row in data:
            flag = True

        conn.close()
        if flag == True:
            welcomewindow()

        else:
            messagebox.showerror("Invalid User Credential", 'Either User Name or Password is incorrect')
            usernameVar.set("")
            passwordVar.set("")

##############  main heading #################################
def mainheading():
    head = Label(taz, text="                           Hotel Taz Management System                       ", fg="green",
                 bg="yellow", font=("Ariel", 24, "bold"))
    head.grid(row=0,column=0,columnspan=4)

##################### login window #######################################
def loginwindow():
    loginLabel = Label(taz, text="Admin Login", font="Arial 30")
    loginLabel.grid(row=1, column=1, columnspan=2, pady=10)

    usernameLabel = Label(taz, text="Username")
    usernameLabel.grid(row=2, column=1, padx=20, pady=5)

    passwordLabel = Label(taz, text="Password")
    passwordLabel.grid(row=3, column=1, padx=20, pady=5)

    global usernameVar
    usernameVar=StringVar()
    usernameEntry = Entry(taz, textvariable=usernameVar)
    usernameEntry.grid(row=2, column=2, padx=20, pady=5)

    global passwordVar
    passwordVar = StringVar()
    passwordEntry = Entry(taz, show="*", textvariable=passwordVar)
    passwordEntry.grid(row=3, column=2, padx=20, pady=5)


    loginButton = Button(taz, text="Login", width=20, height=2, fg="green", bd=10,command=adminlogin)
    loginButton.grid(row=4,column=1,columnspan=2)


################################### admin login process ##################



mainheading()
loginwindow()
taz.geometry("%dx%d+0+0"%(width,height))
taz.resizable(0,0)
mainloop()