from machine import Pin, I2C
from utime import sleep_ms
import sys

# create I2C object
i2c = machine.I2C(0,
                  scl=machine.Pin(17),
                  sda=machine.Pin(16),
                  freq=400000)

# print out any addresses found
devices = i2c.scan()

if devices:
    for d in devices:
        print(hex(d))

# functions to read and write data from specific registers
def reg_write(i2c, addr, reg, data):
    """Write data to the specified register"""
    # construct message
    msg = bytearray()
    msg.append(data)
    
    # write out message to register
    i2c.writeto_mem(addr, reg, msg)
    
def reg_read(i2c, addr, reg, nbytes = 1):
    """Read byte(s) from specified register. If nbytes> 1, read from registers"""
    
    # check to make sure caller is asking for 1 or more bytes
    if nbytes <1:
        return bytearray()
    
    # request data from specified register9s) over i2c
    data = i2c.readfrom_mem(addr, reg, nbytes)
    
    return data

# wait before taking measurements
utime.sleep(2.0)

# event loop
while True:
    # <read i2c data here>
    
    sleep_ms(50)