import time

import random
#Import the module
import Adafruit_MCP4725

#import the ADC module class
import mcp3428
import smbus

# create bus object
bus = smbus.SMBus(1)
# create a dictionary of addresses and information needed for the ADC instance
kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain':0x00}

# crate a ADC instance directing towards the bus with the addresses located in kwargs
mcp3428 = mcp3428.MCP3428(bus, kwargs)

# Create a DAC instance...whatever that means
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

# steps to follow


# start the ramp time, this will be the basis for the slope of the ramp we are running up

# go through the ramp until it hits 1800 volts
#definesa function for the ramp by increment and decrement and the time per increment that we want.
def voltage_ramp(increment, decrement, seconds):
    #sets voltage to zero
    voltage = 0
    #conversion factor of our dac and adc
    conversion_factor = 0.002
    #set the voltage to zero
    dac.set_voltage(voltage)

    #Try it now, this is where the trip will be but I am working on it
    ###starttime = time.time()
    # sleep time for when the trip is enacted
    ###sleeptime = 0
    
    #start timer
    prevTime = time.time()
    #begin while loop of increments and decrements
    while 1:
        # read the voltage and interval, the
        voltageReading = mcp3428.take_single_recording(0)
        voltage = voltageReading
        
        #get the livetime and what until 1 second passes
        livetime = time.time()
        if livetime-prevTime < seconds:
            continue

        #resets the prevTime variable for the next increment
        prevTime = livetime
        print('voltage: ' + str(voltage))

        if voltage < 1800:
            voltage = voltage + increment
            bit = voltage / conversion_factor
            print('bit: ' + str(bit))
            dac.set_voltage(bit)

        elif voltage > 1800:
            voltage = voltage-decrement
            bit = voltage / conversion_factor
            print('bit: ' + str(bit))
            dac.set_voltage(bit)
        else:
            continue

#reset the parameters of the ramp below, then run the function voltage_ramp.exe
if __name__ == '__main__':
    voltage_ramp(1, 1, 1)
