from flask import Flask
import os
import threading
from gpiozero import RGBLED


# led = RGBLED()
app = Flask(__name__)
tea_alert_siren = 'media/siren.mp3'


def tea_alert():
    # turn on led
    os.system("mpg321 " + tea_alert_siren)


@app.route('/')
def index():
    pass


@app.route('/request_tea')
def request_tea():
    th = threading.Thread(target=tea_alert)
    th.start()
    return 'tea request sent'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')