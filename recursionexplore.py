import sys
#sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=1
def msg():
    global i
    print("good afternoon",i)
    i = i + 1
    msg() #again call


msg()
