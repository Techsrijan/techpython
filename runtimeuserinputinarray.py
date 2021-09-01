from array import *
arr=array('i',[])
n=int(input("how many elements u want to store"))

for i in range(n):
    x=int(input("Enter the marks of student"))
    arr.append(x)

print(arr)

max1=arr[0]
for i in range(1,n):
    if arr[i]>max1:
        max1=arr[i]

print(max1)

print("Minimum=",min(arr))
print("Maximum=",max(arr))

findval=int(input("Enter the marks of student u want search"))
pos=0
for i in arr:
    if i==findval:
        print("Item found")
        print("Item Found at location:", pos)
        break
    pos=pos+1
else:
    print("Item not found")


# for search\\
print("Libray find=",arr.index(findval))

