n=int(input("Enter any number ?"))
x=n
sum=0
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=n//10

print("sum of digit=",sum)

if x==sum:
    print("armstrong")
else:
    print("not armstrong")