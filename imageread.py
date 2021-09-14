f=open("TCS.jpg","rb")
f2=open("MyTCS.jpg","wb")
for data in f:
    print(data)
    f2.write(data)