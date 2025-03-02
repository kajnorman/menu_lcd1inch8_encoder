import network
import time

def scan_wifi():
    wlan = network.WLAN(network.STA_IF)  # Station Mode
    wlan.active(True)                   # Aktivér Wi-Fi interface
    print("Scanner efter Wi-Fi netværk...")

    nets = wlan.scan()  # Scan tilgængelige netværk

    for net in nets:
        ssid = net[0].decode("utf-8")  # Netværksnavn (SSID)
        rssi = net[3]                 # Signalstyrke
        sec = net[4]                  # Sikkerhedstype

        # Oversæt sikkerhedstype
        if sec == 0:
            sec_type = "Open"
        elif sec == 1:
            sec_type = "WEP"
        elif sec == 2:
            sec_type = "WPA-PSK"
        elif sec == 3:
            sec_type = "WPA2-PSK"
        elif sec == 4:
            sec_type = "WPA/WPA2-PSK"
        else:
            sec_type = "Ukendt"

        print(f"SSID: {ssid}, Signal: {rssi} dBm, Sikkerhed: {sec_type}")

# Kør scanningen
scan_wifi()
