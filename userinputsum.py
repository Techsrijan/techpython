n=int(input("Enter any number ?"))
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n//10

print("sum of digit=",sum)