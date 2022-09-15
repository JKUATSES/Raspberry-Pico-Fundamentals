from machine import Pin
from utime import sleep_ms
led =2
led_pin = Pin(led, Pin.OUT)

while True:
    led_pin.toggle()
    sleep_ms(400)
    
    