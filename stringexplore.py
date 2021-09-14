st="welcome To python"
print(len(st))
print(st[0:])
print(st)
print(st.swapcase())
print(st.lower())
print(st.upper())
print(st.capitalize())
print(st.split(' '))
print(st.endswith('N'))
print(st.title())
print(st.find('py'))
st2="Her name is tammana and tammana is good girl "
print(st2.replace('tammana','sonia'))
mobile=input("enter your mobile no")
print(mobile)
if mobile.isdigit():
    print("valid")
else:
    print("Galat mobile number")
name=input("enetr your name")
print(name)
#print(name.strip(' '))
print(name.lstrip('!'))
print(name)
print(name.rstrip('!'))
print(name)
if name.isalpha():
    print("sahi hi")
else:
    print("sahai se name enter karo")

