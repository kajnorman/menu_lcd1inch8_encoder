from machine import Pin
import time

#def init():
A = Pin(27, Pin.IN,Pin.PULL_DOWN)
B = Pin(26, Pin.IN,Pin.PULL_DOWN)
#Testpin = Pin(0,Pin.OUT)
Push = Pin(28, Pin.IN, Pin.PULL_UP)  #active low


def UserInput():
    UP=0
    DWN=0
    SELECT=0
    if Push()==0:
        SELECT = 1
        time.sleep(0.6)   # hvis denne tid er for lav så vil man selecte i næste funktion
        return UP,DWN,SELECT
    while A() != 0 or B() != 0: #vent på begge er 0
        if Push() == 0:
            SELECT = 1
            return UP, DWN, SELECT
    time.sleep(0.003)
    newA = A()
    newB = B()
    while (newA == 0) and  (newB == 0): #vent på en af dem er 1
        if Push() == 0:
            SELECT = 1
            return UP, DWN, SELECT
        newA = A()
        newB = B()
    if newA:
        UP=1
    if newB:
        DWN=1
    return UP,DWN,SELECT

