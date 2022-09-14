import machine
import utime

btn = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
# pull doen to hold the button low all the time unless when it is pressed

while True:
    if btn.value() == 1:
        print("pressed")
        
    utime.sleep_ms(300)