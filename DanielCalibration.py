# Python script for user to set voltage.
# Author: Andrew Schick and Daniel Lis
# License: MIT License

import time

#Import the module
import Adafruit_MCP4725

#import the ADC module class
import mcp3428
import smbus

#create bus object 
bus = smbus.SMBus(1)
#create a dictionary of addresses and information needed for the ADC instance
kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain':0x00}

#crate a ADC instance directing towards the bus with the addresses located in kwargs
mcp3428 = mcp3428.MCP3428(bus, kwargs)

# Create a DAC instance...whatever that means
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

#Initialization of variables
previous_reading = 0
current_reading = 0
conversion_factor = .002 #How the readings change when they get read into and out of the ADC
voltage = 0
dac.set_voltage(0) #set the voltage to zero through the dac instance
set_voltage = True
start = time.time() #start the timer to step up the Voltage
previous_reading = mcp3428.take_single_recording(0)

#steps to follow
#1. While loop that keeps on going through
print 'Press ctrl-C to exit...'

while True:
        counter = 0; #inititaite counter for checking the rate at zero
        start = time.time() #start time of loop
        end = time.time() #end time
        breakSafe = True #initiate boolean for the loop break
        while end-start <= 60: #monitor the voltage recording for a minute
                iStart = time.time #start of recording
                previous_reading = mcp3428.take_single_recording(0)
                time.sleep(1)
                current_reading = mcp3428.take_single_recording(0)
                end = time.time() #end recording
                rate = (current_reading - previous_reading)/(end - iStart) #calculate the instantaneous rate of the voltage increase
                #print the rate and the readings
                print 'The Recording:'
                print current_reading
                print '\r\n'
                print '------------'
                print '\r\n'
                print 'The rate:'
                print rate
                print '\r\n'
                print '------------'
                print '\r\n'
                
                if (rate>1): #if the rate exceeds 1 volt per second, as in it jumps past the increase in voltage, it will be done.
                        breakSafe = False
                        break
                if (rate == 0);
                        counter += 1
                        if counter == 5: #if the readings are the same for 5 seconds, we will break and bump
                                breakSafe = True
                                break
        finalVoltage = mcp3428.take_single_recording(0) # final voltage level
        
        if BreakSafe: #if the loop was not broken unsafely, then it is fine
                voltage += 1 #increment voltage by 1
                bit = voltage/conversion_factor #convert to bit through the conversion factor found in the python file
                time.sleep(0.01) #rest
                dac.set_voltage(bit) #set voltage through the dac
                print 'Increasing Voltage by 1'
                time.sleep(0.01)
        else: #if BreakSafe is false, then the voltage will step back down and rest for a minute
                voltage -= 1
                bit = voltage/conversion_factor
                time.sleep(0.01)
                dac.set_voltage(bit)
                print 'Decreasing Voltage by 1'
                time.sleep(60)



