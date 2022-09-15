from machine import Pin, PWM
from utime import sleep_ms

# create a PWM object
led = PWM(Pin(13))

# set pwm frequency
led.freq(1000)

while True:
    # fade and brighten LED
    for duty in range(0, 65535):
        led.duty_u16(duty)
        sleep_ms(10)
