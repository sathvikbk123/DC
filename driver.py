from main import *
from randnogen import *

t=0

def display():
    print("Time at which frames are sent by each station ")
    A.display_station()
    B.display_station()
    C.display_station()
    D.display_station()
    channel.displaychannelstatus()
    print("Initial time of sending frames")
    A.display_orig()
    B.display_orig()
    C.display_orig()
    D.display_orig()
    print("Actual Sent Frames Times")
    A.display_sent()
    B.display_sent()
    C.display_sent()
    D.display_sent()
    print("Recieved Frames Times at reciever")
    W.displayreciever()
    X.displayreciever()
    Y.displayreciever()
    Z.displayreciever()

#initialisation of channels, recievers and stations

A=Station()
B=Station()
C=Station()
D=Station()

time=0

W=Reciever()
X=Reciever()
Y=Reciever()
Z=Reciever()

channel=Channel()


print("Initialisation")

l=randomlist(5)
A.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
B.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
C.frameslotinit(l)
channel.timeslotinit(l)
l=randomlist(5)
D.frameslotinit(l)
channel.timeslotinit(l)

#display()

#End of initialisation

success=1

#ALOHA PROTOCOL


def backoff(S,t,i):
    print("Back off algorithm for time t = ",t)
    S.k+=1
    if S.k<=15:
        R=randrange(0,2**(S.k),1)
        newtime=t+R*5
        print(newtime)
        if (S.frameslotadd(newtime,i))==True:
            channel.timeslotadd(newtime)
        else:
            abort(S,t,i)
    else:
        abort(S,t,i)

def abort(S,t,i):
    S.k=0
    newtime=1000+t
    S.frameslotadd(newtime,i)
    channel.timeslotadd(newtime)

def ifinframeslotsA(t):
    for i in A.frameslots.keys():
        if t in A.frameslots[i]:
            return i
        else:
            pass
    return -1
def ifinframeslotsB(t):
    for i in B.frameslots.keys():
        if t in B.frameslots[i]:
            return i
        else:
            pass
    return -1
def ifinframeslotsC(t):
    for i in C.frameslots.keys():
        if t in C.frameslots[i]:
            return i
        else:
            pass
    return -1
def ifinframeslotsD(t):
    for i in D.frameslots.keys():
        if t in D.frameslots[i]:
            return i
        else:
            pass
    return -1

while(t<10000):
    t+=1
    if t not in channel.timeslots:
        pass
    else:
        if t in channel.common:
            temp=t+10 #Changelog -> replaced t by temp in backoff functions
            tempA=ifinframeslotsA(t)
            tempB = ifinframeslotsB(t)
            tempC = ifinframeslotsC(t)
            tempD = ifinframeslotsD(t)

            if tempA!=-1:
                #A.frameslotdel(t)
                backoff(A,temp,tempA)
            if tempB!=-1:
                #B.frameslotdel(t)
                backoff(B,temp,tempB)
            if tempC!=-1:
                #C.frameslotdel(t)
                backoff(C,temp,tempC)
            if tempD!=-1:
                #D.frameslotdel(t)
                backoff(D,temp,tempD)

        else:
            temp=t+10
            if t in A.frameslots:
                A.sentframes.append(t)
                W.recieveframe(temp)
            if t in B.frameslots:
                B.sentframes.append(t)
                X.recieveframe(temp)
            if t in C.frameslots:
                C.sentframes.append(t)
                Y.recieveframe(temp)
            if t in D.frameslots:
                D.sentframes.append(t)
                Z.recieveframe(temp)


display()