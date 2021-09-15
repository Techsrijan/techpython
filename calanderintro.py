#import calendar
from calendar import *
#print(calendar.month(2100,2))
#print(calendar(2021))

ww=weekday(2001,10,10)
print(weekday(2001,10,10))

y,m,d=input("Enter your date of birth seprated by -").split('-')
a=weekday(int(y),int(m),int(d))
if a==0:
    print("monday")
elif a==1:
    print("Tuesday")
elif a==2:
    print("wednesday")
print(isleap(2000))
print(leapdays(1900,2021))
