from PyQt5 importQtCore,QtGui,QtWidgets
'''usr code'''
importRPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led = LED(23) #for the led toggling proj

led_pin = 24 #for LED DImmer
GPIO.setup(led_pin,GPIO.OUT)
pwm = GPIO.PWM(led_pin,100)
pwn.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()
'''usr code'''

