from machine import Pin
import time

#def init():
A = Pin(27, Pin.IN,Pin.PULL_DOWN)
B = Pin(26, Pin.IN,Pin.PULL_DOWN)
#Testpin = Pin(0,Pin.OUT)
Push = Pin(28, Pin.IN, Pin.PULL_UP)  #active low


def UserInput():
        while A() != 0 or B() != 0  or Push()!= 1: #vent på alle signaler er passive
            pass  #gør ingenting
        time.sleep(0.02)  # vent på prell
        UP = 0
        DWN = 0
        SELECT = 0
        while True:
            if Push() == 0:
                SELECT = 1
                time.sleep(0.02)  # vent på prell
                return UP, DWN, SELECT
            if A():
                UP = 1
                time.sleep(0.02)  # vent på prell
                return UP, DWN, SELECT
            if B():
                DWN = 1
                time.sleep(0.02)  # vent på prell
                return UP, DWN, SELECT


