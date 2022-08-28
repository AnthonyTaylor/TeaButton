from flask import Flask
import os
import threading
from gpiozero import RGBLED


# led = RGBLED()
app = Flask(__name__)
tea_alert_siren = 'media/siren.mp3'


@app.route('/')
def index():
    pass


@app.route('/yes')
def request_tea():
    # make led green
    return 'response recieved'


@app.route('/no')
def request_tea():
    # make led red
    return 'response recieved'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')