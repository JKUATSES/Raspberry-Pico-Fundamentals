from machine import ADC, Pin
from utime import sleep_ms

conversion_factor = 3.3/65535
pot = ADC(27)
/
while True:
    pot_value = pot.read_u16()
    voltage = pot_value * conversion_factor
    print(voltage)
    sleep_ms(10)
    