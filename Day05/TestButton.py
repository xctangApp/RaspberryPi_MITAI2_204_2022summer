#204 Test a button
#Date: 2022-07-22
#Owner: X.Tang
#Version: 1.0

from gpiozero import Button

btn = Button(5)

def hello():
    print('Hello')

btn.when_pressed = hello
