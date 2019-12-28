import RPi.GPIO as GPIO
import time
import requests

SWITCH_BUTTON=21

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(21)
    if input_state == False:
        print('Button Pressed')
        r = requests.get('http://192.168.5.66/cm?cmnd=Power%20TOGGLE')
        requests.get('https://api.github.com')
        time.sleep(0.2)
