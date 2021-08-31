n=int(input("How many toffe u want ?"))
stock=15
count=1
while count<=n:
    if stock>=count:
        print("Please collect toffee=",count)

    else:
        print("Out of stock")
        break
    count=count+1
else:  # when loop properly runs
    print("thanks Please visit again")
