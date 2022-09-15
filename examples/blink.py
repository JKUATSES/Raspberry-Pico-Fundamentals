import machine
import utime

led_pin = machine.Pin(10, machine.Pin.OUT)

while True:
    led_pin.value(1)
    utime.sleep_ms(500)
    led_pin.value(0)
    utime.sleep(500)

    # version 2
    # led_pin.toggle();
    # utime.sleep_ms(300)


