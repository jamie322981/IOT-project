from boot import connection
from time import sleep
from machine import Pin, ADC
import urequests as requests
import json
import config

# Functie om de temperatuur te lezen
def read_temperature():
    tmp36 = Pin(34, Pin.IN)
    adc = ADC(tmp36)
    prop = 1100 / 65535
    v_out = adc.read_u16() * prop
    temp = (v_out - 500) / 10
    return temp

# Functie om de blauwe LED te laten knipperen
def flash_blue_led():
    led = Pin(2, Pin.OUT)
    led.on()
    sleep(0.1)
    led.off()

# Functie om de rode LED in te stellen of uit te schakelen op basis van de serverrespons
def control_red_led(response):
    led = Pin(32, Pin.OUT)
    if response.get("set_red_led"):
        led.on()
    else:
        led.off()

while connection.isconnected():
    # Lees de temperatuur
    temperature = read_temperature()

    # Maak JSON-bericht met de temperatuur en LED-status
    message = {"temperature": temperature, "red_led_status": "on"}  # Stel hier de LED-status in

    try:
        # Stuur het bericht naar de server
        url = f"http://{config.SERVER}:{config.PORT}{config.ENDPOINT}"
        response = requests.post(url, json=message)

        # Laat de blauwe LED knipperen om aan te geven dat de temperatuur is verzonden
        flash_blue_led()

        # Lees de serverrespons
        response_data = response.json()

        # Controleer en stel de rode LED in op basis van de serverrespons
        control_red_led(response_data)
    except Exception as e:
        print("Error:", e)

    # Wacht even tot de volgende temperatuurmeting
    sleep(1)  # Wacht 60 seconden voordat je de volgende meting doet
