import time
from machine import Pin, PWM
from menuclass import Menu, menuItem ,getnumber

import UI


from LCD_1_8_file import LCD_1inch8


BL = 13

if __name__ == '__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)  # max 65535


def f1():
    print("Hej fra f1")
    time.sleep(0.5)

def f2():
    print("Hej fra f2")
    time.sleep(0.5)


mp1 = menuItem("mp1-object",f1)
mp2 = menuItem("mp2-object",f2)

mainmenu = Menu()
mainmenu.AddMenuItem(mp1)
mainmenu.AddMenuItem(mp2)


submenu1 = Menu()
submenu1.AddMenuItem(mp1)
submenu1.AddMenuItem(mp1)
submenu1.AddMenuItem(mp2)
submenu1Item = menuItem("sub menu 1",submenu1.execute)
mainmenu.AddMenuItem(submenu1Item)


enteritem = menuItem("enter digit",getnumber)


submenu2 = Menu()
submenu2.AddMenuItem(mp2)
submenu2.AddMenuItem(mp2)
submenu2.AddMenuItem(mp1)
submenu2Item = menuItem("gpio menu",submenu1.execute)



mainmenu.AddMenuItem(submenu2Item)
mainmenu.AddMenuItem(enteritem)

mainmenu.execute()

