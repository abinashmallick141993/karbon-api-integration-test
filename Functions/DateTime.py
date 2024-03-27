import datetime


Now = datetime.datetime.now()
def DateTime():
    Year=Now.strftime("%Y")
    Month=Now.strftime("%m")
    Day=Now.strftime("%d")
    Hour=Now.strftime("%H")
    Min=Now.strftime("%M")
    # print(Now)
    # print(Year)
    # print(Month)
    # print(Day)
    # print(Hour)
    # print(Min)
    #Date=print(Year,"-",Month,"-",Day)
    #print(Now.__eq__(Date))
    Time=Now.strftime("%y-%m-%d")
    #print(Time)
DateTime()

def Date():
    Today=Now.strftime("%y-%m-%d")
    #print(Today)
Date()

def Time():
    Tim=Now.strftime("%H-%M-%S")
    #print(Tim)
Time()

def DateAndTime():
    Runntime=Now.strftime("%y-%m-%d %H:%M:%S")
    #print(Runntime)
DateAndTime()
