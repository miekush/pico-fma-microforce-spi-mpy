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
    #read sensor
    status, force, temp = fma1.read()
    print("Status: " + status + ", Force: " + str(force) + " N, Temp: " + str(temp) + " °C")
    #print(fma1.pressed())
    time.sleep(0.1)