from gpiozero import Button
import requests
import time

btn_yes = Button(17)
btn_no = Button(18)
endpoint = '192.168.1.146:5000/'

while True:
    if btn_yes.is_pressed:
        requests.get(endpoint + 'yes')
        time.sleep(5)
    if btn_no.is_pressed:
        requests.get(endpoint + 'no')
        time.sleep(5)