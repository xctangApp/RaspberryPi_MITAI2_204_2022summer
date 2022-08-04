#--------------------------------------------------------
#
#       LED Control from android app
#
#
# In this project, 3 LEDs are connected to ports GPIO 2,3,4
# of Raspberry Pi through a current limiting ressitor.
# The LED is turned ON and OFF from android app
#
#
# Program: LEDAppControl_traffic_WiFi.py
# Date   : 07/27/2022
# Author : Xincheng Tang
#---------------------------------------------------------

from flask import Flask,render_template  # import Flask library
import RPi.GPIO as GPIO

app=Flask(__name__)

GPIO.setwarnings(False)   # disable warnings
GPIO.setmode(GPIO.BCM)    # set BCM pin numbering

LED1 = 2                   # LED on GPIO 2
LED2 = 3                   # LED on GPIO 3
LED3 = 4                   # LED on GPIO 4

GPIO.setup(LED1, GPIO.OUT) # conf LED1 as output
GPIO.setup(LED2, GPIO.OUT) # conf LED2 as output
GPIO.setup(LED3, GPIO.OUT) # conf LED3 as output

GPIO.output(LED1, 0)       # turn off LED1 to start with
GPIO.output(LED2, 0)       # turn off LED2 to start with
GPIO.output(LED3, 0)       # turn off LED3 to start with

#
# start of the main program loop, read commands from
# the android mobile phone, decode them and control LED
#

@app.route("/<device>/<action>")
def action(device, action):
       actuator = LED1
       if action == "on1":
          GPIO.output(actuator, GPIO.HIGH)     #LED1 on
       if action == "off1":
          GPIO.output(actuator, GPIO.LOW)      #LED1 off 

       actuator = LED2
       if action == "on2":
          GPIO.output(actuator, GPIO.HIGH)     #LED2 on
       if action == "off2":
          GPIO.output(actuator, GPIO.LOW)      #LED2 off
         
       actuator = LED3
       if action == "on3":
          GPIO.output(actuator, GPIO.HIGH)     #LED3 on
       if action == "off3":
          GPIO.output(actuator, GPIO.LOW)      #LED3 off
          
       return ""

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')









