from machine import SPI, I2C, Pin
from microforce_spi import MicroForceSensor
from ssd1306 import SSD1306_I2C
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

#create instance of I2C class
i2c = I2C(1, sda=Pin(6), scl=Pin(7))

#create instance of SSD1306 class
display = SSD1306_I2C(128, 64, i2c)

#zero sensor output
fma1.zero()

while 1:
    #read sensor
    status, force, temp = fma1.read()
    display.fill(0)
    display.text('MicroForce Test', 4, 0, 1)
    display.text("Status: " + status, 0, 15, 1)
    display.text("Force: " + str(force) + " N", 0, 30, 1)
    display.text("Temp: " + str(temp) + " C", 0, 45, 1)
    display.show()
    time.sleep(0.1)