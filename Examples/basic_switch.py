#Raspberry Pi Pico Honeywell FMA Microforce SPI MicroPython Module Example Usage
#Device: RP2040, Honeywell FMA Microforce
#File: main.py
#Author: Mike Kushnerik
#Date: 10/5/2022

from machine import SPI, Pin
from microforce_spi import MicroForceSensor
import time

#create instance of SPI class
spi = SPI(0, 100000, sck=Pin(2), miso=Pin(4))

#create instance of MicroForceSensor class
fma1 = MicroForceSensor(
    #pico spi pins
    spi, cs = 5,
    #25N
    force_range = 25,
    #20% -> 80%, see sensor datasheet
    transfer_func = 'C')

#zero sensor output
fma1.zero()

while 1: 
    #read switch
    print(fma1.pressed())
    time.sleep(0.1)