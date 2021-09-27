import pymysql

try:
    connection=pymysql.connect(host="localhost",user="root",db="pythonbatch")
    print("connection established")
    #query="create table login_info(userid varchar(20),password varchar(10))"
    a,b=input("enetr user id and password").split(",")
    insquery="insert into login_info(userid,password) values(%s,%s)"
    val=(a,b)
    mycursor=connection.cursor()
    mycursor.execute(insquery,val)
    connection.commit() # to save insert update delete
    print("data inserted successfully")

    que = "select * from login_info"
    mycursor.execute(que)
    result = mycursor.fetchall()
    print(result)
except Exception:
    print("Sql server not on")
    print("something went wrong")
finally:
    pass
    #connection.close()
