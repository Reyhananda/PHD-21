# import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo


from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo_bawah = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)
servo_atas = Servo(11, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)