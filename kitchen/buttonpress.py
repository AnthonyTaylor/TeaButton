# This file will need to be run on start up
# Press button to hit server on on other device


from gpiozero import Button
import requests
import time

btn_request = Button(17)

while True:
    if btn_request.is_pressed:
        requests.get('127.0.0.1:5000/request_tea')
        time.sleep(5)