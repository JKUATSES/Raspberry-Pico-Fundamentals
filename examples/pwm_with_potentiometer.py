from machine import Pin, ADC, PWM
from utime import sleep_ms

led = PWM(Pin(13))
led.freq(1000) # set LED frequency

pot = ADC(28) # create potentiometer object at ADC Pin 28

while True:
    pot_value = pot.read_u16()
    print(pot_value)
    
    led.duty_u16(pot_value)
    
    sleep_ms(5)