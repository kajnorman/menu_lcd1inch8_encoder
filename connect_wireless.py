import network
import time

wlan = None

def getip():
    global wlan
    #print("IP:", wlan.ifconfig()[0])
    return str(wlan.ifconfig()[0])

def connect():
    global wlan
    # Netværksoplysninger
    SSID = "your AP SSID"
    PASSWORD = "Your Pass"

    # Opret netværksinterface
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # Forbind til Wi-Fi
    if not wlan.isconnected():
        print("Forbinder til netværk...")
        wlan.connect(SSID, PASSWORD)

        # Vent på forbindelse
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            print("Venter på forbindelse...")
            time.sleep(1)
            timeout -= 1

    if wlan.isconnected():
        print("Forbundet til netværk")
        getip()
    else:
        print("Kunne ikke forbinde til netværket")

