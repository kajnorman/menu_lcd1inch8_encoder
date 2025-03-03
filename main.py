import time
from machine import Pin, PWM
from menuclass import Menu, menuItem ,getnumber, writestr
import connect_wireless


from LCD_1_8_file import LCD_1inch8

BL = 13

if __name__ == '__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)  # max 65535


############################################
def f1():
    print("Hej fra f1")
    time.sleep(0.5)

def f2():
    print("Hej fra f2")
    time.sleep(0.5)

def setPinHi():
    n = getnumber()
    p = Pin(n,Pin.OUT)
    p(1)

def setPinLo():
    n = getnumber()
    p = Pin(n,Pin.OUT)
    p(0)

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

enteritem = menuItem("test of enter digit",getnumber)
setpinhiItem = menuItem('set a gp pin hi',setPinHi)
setpinloItem = menuItem('set a gp pin low',setPinLo)

submenu_gpio = Menu()
submenu_gpio.AddMenuItem(enteritem)
submenu_gpio.AddMenuItem(setpinhiItem)
submenu_gpio.AddMenuItem(setpinloItem)
submenu_gpioItem = menuItem("gpio menu",submenu_gpio.execute)
mainmenu.AddMenuItem(submenu_gpioItem)

ServoPinNumber = 0

enterservopinnr_Item = menuItem("Enter servo pinnumber",getnumber)
submenu_servo = Menu()
submenu_servo.AddMenuItem(enterservopinnr_Item)
#submenu_servo.AddMenuItem(setpinhiItem)
submenu_servoItem = menuItem("servo menu",submenu_servo.execute)
mainmenu.AddMenuItem(submenu_servoItem)

####################    wireless menu###
Conect_wlan_Item = menuItem("Connect to wireless Network",connect_wireless.connect)
#getIP_wlan_Item = menuItem("Show IP",connect_wireless.connect)
#getIP_wlan_Item = menuItem("Show IP",lambda topic, msg: print(f"Modtaget '{msg.decode()}' på '{topic.decode()}'"))
#getIP_wlan_Item = menuItem("Show IP",lambda : print(f"Modtaget IP '{connect_wireless.getip()}'"))
getIP_wlan_Item = menuItem("Show IP",lambda : writestr(f"IP'{connect_wireless.getip()}'"))
submenu_wifi = Menu()
submenu_wifi.AddMenuItem(Conect_wlan_Item)
submenu_wifi.AddMenuItem(getIP_wlan_Item)
submenuwifiItem= menuItem("Wifi menu",submenu_wifi.execute)
#submenu_wifi_item = mainmenu.AddMenuItem(submenu_wifi)
mainmenu.AddMenuItem(submenuwifiItem)



print ('mainmenu starter')

mainmenu.execute()

print ('mainmenu slutter')
