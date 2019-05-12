from randnogen import *


class Channel:


    def __init__(self,a=5):
        self.no_of_channels=a
        self.timeslots=[]
        self.common=[]

    # i not in self.common -> check

    def timeslotinit(self,l):
        for i in l:
            if i not in self.timeslots:
                self.timeslots.append(i)
            elif i in self.timeslots and i not in self.common:
                self.common.append(i)
                self.common.sort()
        self.timeslots.sort()

    def timeslotadd(self,n):
        if n not in self.timeslots:
            self.timeslots.append(n)
        elif n in self.timeslots and n not in self.common:
            self.common.append(n)
            self.common.sort()
        self.timeslots.sort()

    def ischannelfree(self,time):
        if time not in self.timeslots:
            return True
        else:
            return False

    def displaychannelstatus(self):
        print("Channel : ",self.timeslots)
        print("Common : ",self.common)




class Station:


    def __init__(self):
        self.no_of_requests=0
        self.frameslots={1:[],2:[],3:[],4:[],5:[]}
        self.frameslotorig=[]
        self.sentframes=[]
        self.k=0
        self.num=0

    def frameslotinit(self,framelist):
        framelist.sort()
        for i in range(1,6):
            self.frameslots[i].append(framelist[i-1])
        #self.frameslots=framelist
        for i in range(1,6):
            self.frameslots[i].sort()
        self.frameslotorig=list(self.frameslots)

    def frameslotadd(self,newtime,i):
        #True False not needed? Verify
        if newtime in self.frameslots[i]:
            return False
        else:
            self.frameslots[i].append(newtime)
            #self.frameslots.sort()
            return True

    def frameslotdel(self,time):
        self.frameslots.remove(time)

    def display_station(self):
        print(self.frameslots)

    def display_orig(self):
        print(self.frameslotorig)

    def display_sent(self):
        print(self.sentframes)





class Reciever:


    def __init__(self):
        self.recieved=[]

    def sendack(self):
        return self.recieved[-1]

    def recieveframe(self,time):
        self.recieved.append(time)

    def displayreciever(self):
        print(self.recieved)



"""
channel=Channel()
A=Station()
B=Station()
l1=randomlist(10)
l2=randomlist(10)
A.frameslotinit(l1)
B.frameslotinit(l2)
channel.timeslotinit(l1)
channel.timeslotinit(l2)
A.frameslotadd(140)
channel.timeslotadd(140)
A.display_station()
B.display_station()
channel.displaychannelstatus()
print("hi")
"""