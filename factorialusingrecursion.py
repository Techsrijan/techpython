def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=int(input("enter the number for which u want to calculate factorial"))
print(fact(n))