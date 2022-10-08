#Raspberry Pi Pico Honeywell FMA Microforce SPI MicroPython Module Example Usage
#Device: RP2040, Honeywell FMA Microforce
#File: main.py
#Author: Mike Kushnerik
#Date: 10/5/2022

#import microforce module
from microforce_spi import MicroForceSensor

#create instance of MicroForceSensor class
fma1 = MicroForceSensor(
    #pico spi instance
    spi_instance = 0,
    #pico spi pins
    miso = 4, sck = 2, cs = 5,
    #25N
    force_range = 25,
    #20% -> 80%, see sensor datasheet
    transfer_func = 'C')

#zero sensor output
fma1.zero()

while 1: 
    #check if sensor is pressed
    print(fma1.pressed())
    time.sleep(0.1)