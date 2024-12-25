import network
import json
import requests
import machine, neopixel
import time
import json
import os

wlan = network.WLAN(network.STA_IF)

def connect():
    with open('wlan.json') as f:
        credentials = json.load(f)
        wlan.connect(credentials['ssid'], credentials['password'])

def set_wifi(ssid, password):
    with open('wlan.json', 'w') as f:
        f.write(json.dumps({
            "ssid": ssid,
            "password": password
        }))
        
def do():
    while True:
        response = requests.get("https://yourURLHere")
        response_content = json.loads(response.content)

        np = neopixel.NeoPixel(machine.Pin(0), 10)

        for light in response_content:
            np[int(light)] = tuple(response_content[light])

        np.write()
        time.sleep(60)

def init():
    # Connect to network
    wlan.active(True)

    if not "wlan.json" in os.listdir():
        print("Use set_wifi(ssid, password) to set a wifi password")
        print("Afterwards reboot")
        return

    connect()

    while not wlan.isconnected():
        pass

    do()

init()
