#Raspberry Pi Pico Honeywell FMA Microforce SPI MicroPython Module
#Device: RP2040, Honeywell FMA Microforce
#File: microforce_spi.py
#Author: Mike Kushnerik
#Date: 10/5/2022

from machine import Pin
import time

#class for Honeywell FMA MicroForce Sensors
class MicroForceSensor:
    #see SPI communcations technical paper
    status_values = {
        0b00: "Normal Mode",
        0b01: "Command Mode",
        0b10: "Data Stale",
        0b11: "Diagnostic Mode"}
    #constructor
    def __init__(self, spi, cs, force_range=5, transfer_func='A', offset=0, threshold=0.1, pressed_threshold=0.2):
        self.spi = spi
        self.cs = Pin(cs, mode=Pin.OUT, value=1)
        #check sensor transfer function
        if transfer_func == 'A':
            self.output_min = 16384 * 0.1
            self.output_max = 16384 * 0.9
        elif transfer_func == 'C':
            self.output_min = 16384 * 0.2
            self.output_max = 16384 * 0.8
        else:
            print("Invalid sensor transfer function selection! See sensor datasheet.")
            quit()
        self.force_rated = force_range
        self.offset = offset
        #minimum threshold for sensing
        self.threshold = threshold
        #minimum threshold for being pressed
        self.pressed_threshold = pressed_threshold
    
    #read all data from sensor
    def read(self, dec=2):
        self.cs(0)
        sensor_data = self.spi.read(4)
        self.cs(1)
        #get sensor status
        status_raw = sensor_data[0] >> 6
        status = self.status_values[status_raw]
        #get force sensor reading
        force_raw = (((sensor_data[0] & 0b111111) << 8) | sensor_data[1]) - self.offset
        force_n = ((force_raw - self.output_min) / (self.output_max - self.output_min)) * self.force_rated
        force_n = round(force_n, dec)
        #get temperature sensor reading
        temperature = (((sensor_data[2] << 3) | (sensor_data[3] >> 5)) / 2047) * 200 - 50
        temperature = round(temperature, dec)
        if force_n < self.threshold:
            force_n = 0
        return status, force_n, temperature
    
    #read force only (2 bytes)
    def read_force(self, raw = False, dec=2):
        self.cs(0)
        sensor_data = self.spi.read(2)
        self.cs(1)
        force_raw = (((sensor_data[0] & 0b111111) << 8) | sensor_data[1]) - self.offset
        force_n = ((force_raw - self.output_min) / (self.output_max - self.output_min)) * self.force_rated        
        force_n = round(force_n, dec)
        if force_n < self.threshold:
            force_n = 0
        if raw:
            return force_raw
        else:
            return abs(force_n)
    
    #read internal temp sensor
    def read_temperature(self, dec=2):
        self.cs(0)
        sensor_data = self.spi.read(4)
        self.cs(1)
        temperature = (((sensor_data[2] << 3) | (sensor_data[3] >> 5)) / 2047) * 200 - 50
        temperature = round(temperature, dec)
        return temperature        
    
    #zero sensor
    def zero(self, num_samples=20):
        samples = []
        i=0
        for i in range(num_samples):
            samples.append(self.read_force(raw=True) - self.output_min)
            time.sleep(0.1)
        self.offset = sum(samples) / len(samples)
    
    #check if sensor is being pressed
    def pressed(self):
        return (self.read_force() > self.pressed_threshold)
    
    #print sensor instance information
    def __str__(self):
        return "TODO"