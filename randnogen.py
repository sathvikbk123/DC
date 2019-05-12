from random import *

def randomno():
    a=randrange(1,51,1)
    return a

def randomlist(a=10):
    l=[]
    x=0
    while (x<a):
        b=randrange(1,51,1)
        if b in l:
            pass
        else:
            l.append(b)
            x+=1
    return l


#print(randomno())
#print(randomlist(100))
