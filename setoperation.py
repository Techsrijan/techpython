s={1,2,34,6}
print(s)
#s[0]=66
s.add(55)
print(s)
s.remove(2)
print(s)
print(s.clear())

#union
a={1,2,34,5,6}
b={5,8,9,1,2}
print(a|b)

#intersection
print(a&b)

# difference
print(a-b)    #whic are in a but not in b
print(b-a)

#symmetric difference
print(a^b)   #3 not common in a and b