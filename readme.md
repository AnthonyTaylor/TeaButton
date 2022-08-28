# Tea Button
## What is it?
A system to request tea for someone in the garage
A Raspberry Pi by the kettle has a non latching button and an RGBLED
A second Raspberry Pi has 2 buttons, a speaker, and an RGBLED
## Process
When someone goes to make a cuppa, they push the button on the Raspberry Pi by the kettle
This will send a request to the other Pi which will alert me to the request.
The 'Yes' or 'No' button will then be pressed, sending the response back to the Pi by the kettle
This will turn on the RGBLED and give it red for 'no' and green for 'yes'
## How to use
This only uses python modules pre-installed on Raspberry OS
Put the /kitchen folder onto the pi intended for the ketchen
configure the buttonpress.py, and the webserver.py files to run on start up and port number
Run '''ifconfig''' to get the ip address

replicate the above steps for the garage Pi, using the /garage folder

in the garage buttonpress.py update the endpoint to the ip address and port number of the kitchen Pi

in the kitchen buttonpress.py update the endpoint to the ip address and port number of the garage Pi

