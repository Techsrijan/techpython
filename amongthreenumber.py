a=int(input("Enter First Number"))
b=int(input("enter Second Number"))
c=int(input("enter Third Number"))
print("A=",a,"B=",b,"C=",c)

if a>b:
    if a>c:
        print("A is greatest")
    else:
        print("C is greatest")
elif b>c:
    print("B is greatest")
else:
    print("C is greatest")