# Raspberry Pi Pico Honeywell FMA Microforce SPI MicroPython Module

This is a Raspberry Pi Pico MicroPython module for the Honeywell FMA Microforce series force sensors using SPI interface

# Example Usage

```python
from microforce_spi import MicroForceSensor

fma1 = MicroForceSensor(
    spi_instance = 0,
    miso = 4, sck = 2, cs = 5,
    #25N
    force_range = 25,
    #20% -> 80%, see sensor datasheet
    transfer_func = 'C')

fma1.zero()

while 1: 
    status, force, temp = fma1.read()
    print("Status: " + status + ", Force: " + str(force) + " N, Temp: " + str(temp) + " °C")
    time.sleep(0.1)
```

# Wiring

By default, Pico SPI instance 0 is used, however this can be changed in the constructor along with the MISO, SCK, and CS pins.

# Breakout

To help with evaluation, I designed a simple breakout in KiCad that supports all variants of the FMA series. See the repo for design files and ordering info.

# Installation

1. Clone repo to a folder of your choice
2. Copy the "microforce_spi.py" file to your Pico
3. Copy one of the example scripts or create your own following the example usage shown above
4. Enjoy! :)

# License

MKE supports the open source hardware community by sharing hardware design files freely on GitHub!

Please support MKE by purchasing products on [Tindie](https://www.tindie.com/stores/mkengineering/)!

Designed by Mike Kushnerik (miekush)

Licensed under [Creative Commons Attribution-ShareAlike CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/)

All text above must be included in any redistribution!
