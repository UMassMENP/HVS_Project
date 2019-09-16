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
while True:
        counter = 0;
        start = time.time()
        end = time.time()
        breakSafe = True
        while end-start <= 60:
                iStart = time.time
                previous_reading = mcp3428.take_single_recording(0)
                time.sleep(1)
                current_reading = mcp3428.take_single_recording(0)
                end = time.time()
                rate = (current_reading - previous_reading)/(end - iStart)
                
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
                
                if (rate>1):
                        breakSafe = False
                        break
                if (rate == 0);
                        counter += 1
                        if counter == 5:
                                breakSafe = True
                                break
        finalVoltage = mcp3428.take_single_recording(0)
        if BreakSafe:
                voltage += 1
                bit = voltage/conversion_factor
                time.sleep(0.01)
                dac.set_voltage(bit)
                print 'Increasing Voltage by 1'
                time.sleep(0.01)
        else:
                voltage -= 1
                bit = voltage/conversion_factor
                time.sleep(0.01)
                dac.set_voltage(bit)
                print 'Decreasing Voltage by 1'
                time.sleep(0.01)
        if 
#2. second while loop that goes until it levels off or goes too fast ( like a minute or so )
#2a. start timer
#2b. get reading
#2c. wait for a second
#2d. get second reading
#2e. end timer
#2f. calculate rate
#2g. print rate and print reading
#2h. if the rate is too fast break and set breakUnsafe to 1
#2i. if the rate is zero add 1 to the counter
#2j. if the counter reaches 5, set breakSafe to 1
#2h. end the inner loop
#3.If statement
#3a. breakSafe = 1
#3ai. set voltage Up one
#3b. breakUnsafe = 1
#3bi. set the new voltage down 1
#Go bakc to the start of the loop



print('Press Ctrl-C to quit...')
while True:
    #Get the reading on just on channel, channel 0 is the first channel on the device.
    #get the rate at which the voltage increased
    current_reading = mcp3428.take_single_recording(0) #channel 0 reading from adc
    end = time.time()#end timer
    time_interval = end - start #find duration of timer
    rate = (current_reading - previous_reading)/time_interval #math to find rate of voltage increase
    save_reading = current_reading
    
    print 'Channel 0 reading: '
    print current_reading
    print '\r\n'
    print 'Rate of Increase: '
    print rate
    print '\r\n'

    if (rate > 2): # change to a waiting period to level out the voltage after the current spike
        voltage -= 1
        bit = voltage/conversion_factor
        time.sleep(0.01)
        dac.set_voltage(bit)
        time.sleep(0.01)
    elif (rate == 0):
        voltage += 1
        bit = voltage/conversion_factor
        time.sleep(0.01)
        dac.set_voltage(bit)
        print 'Increasing Voltage by 1'
        time.sleep(0.01)

    start = time.time()
    time.sleep(1)

while 
