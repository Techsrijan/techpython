try:
    print("frzee is open ")
    a=int(input("Enter First Number"))
    b=int(input("enter Second Number"))
    print("A=",a,"B=",b)

    d = a / b
    print("div=", d)

    #print("frzee is close ")


except ZeroDivisionError :
    print("b can not be zero")


except ValueError :
    print("You have entered a character")

except Exception:
    print("something went wrong")

finally:
    print("frzee is close ")


