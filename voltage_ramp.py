import time
#Import the module
import Adafruit_MCP4725

#import the ADC module class
import mcp3428
import smbus
import trip

# create bus object
bus = smbus.SMBus(1)
# create a dictionary of addresses and information needed for the ADC instance
kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain':0x00}

# crate a ADC instance directing towards the bus with the addresses located in kwargs
mcp3428 = mcp3428.MCP3428(bus, kwargs)

# Create a DAC instance...whatever that means
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

# Initialization of variables

conversion_factor = .002  # How the readings change when they get read into and out of the ADC
voltage = 0
dac.set_voltage(0)  # set the voltage to zero through the dac instance

# steps to follow

# 1. While loop that keeps on going through
print('Press ctrl-C to exit...')

# start the ramp time, this will be the basis for the slope of the ramp we are running up
startTime = time.time()
# sleep time for when the trip is enacted
sleepTime = 0
# go through the ramp until it hits 1800 volts
while voltage < 1800:
    # read the voltage and interval, the
    voltageReading = mcp3428.take_single_recording(0)
    liveTime = time.time()
    elapsedTime = liveTime - startTime - sleepTime
    if (voltageReading - elapsedTime) < 1:
        voltage += 1
        bit = voltage / conversion_factor
        dac.set_voltage(bit)
        print('Increasing Voltage to ' + voltage)
    elif (voltageReading - elapsedTime) > 1:
        voltage -= 1
        bit = voltage / conversion_factor
        dac.set_voltage(bit)
        print('Decreasing Voltage to ' + voltage)
        time.sleep(10)
        sleepTime += 10

while True:
    while voltage > 1800:
        voltage -= 1
        bit = voltage / conversion_factor
        dac.set_voltage(bit)
        print('Decreasing voltage down to ' + voltage)
        time.sleep(1)
    while voltage < 1800:
        voltage += 1
        bit = voltage / conversion_factor
        dac.set_voltage(bit)
        print('Increasing voltage up to ' + voltage)
        time.sleep(1)




