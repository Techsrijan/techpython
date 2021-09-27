from tkinter import *
import pymysql
root=Tk()
def get_data():
    if s.get()=='' or s1.get()=='':
        print("Please fill the value")
    a=s.get()
    s.set('')
    b=s1.get()
    s1.set('')
    connection = pymysql.connect(host="localhost", user="root", db="pythonbatch")
    mycursor = connection.cursor()
    insquery = "insert into login_info(userid,password) values(%s,%s)"
    val = (a, b)
    mycursor.execute(insquery, val)
    connection.commit()  # to save insert update delete

l=Label(root,text="Enter Your User Name",bg="yellow", fg="red",
        font=("Comic Sans Ms", 15, "bold"))
l.grid(row=0,column=0)
s=StringVar()
text1=Entry(root,font=("Comic Sans Ms", 15, "bold"),textvariable=s)
text1.grid(row=0,column=1)

l1=Label(root,text="Enter Your Password",bg="yellow", fg="red",
        font=("Comic Sans Ms", 15, "bold"))
l1.grid(row=1,column=0)
s1=StringVar()
text2=Entry(root,font=("Comic Sans Ms", 15, "bold"),show="*",textvariable=s1)
text2.grid(row=1,column=1)

btn=Button(root,text="Save Data",bg="yellow",fg="red",
           font=("Comic Sans Ms",12,"bold"),command=get_data)
btn.grid(row=2,column=0)


mainloop()