n=1
sum=0
while n<=10:
    if n % 2 == 0:
        print("even no=",n)
        sum=sum+n
        print("sum inside=",sum)
    else:
        print("odd no=",n)
    n=n+1

print(sum)