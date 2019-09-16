# Python script for user to set voltage.
# Author: Andrew Schick
# License: MIT License

import time

#Import the module
import Adafruit_MCP4725

#import the ADC module class
import mcp3428
import smbus

bus = smbus.SMBus(1)

kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain':0x00}

mcp3428 = mcp3428.MCP3428(bus, kwargs)

# Create a DAC instance...whatever that means
dac = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

previous_reading = 0
conversion_factor = .002
voltage = 0
dac.set_voltage(0)
set_voltage = True
start = time.time()

print('Press Ctrl-C to quit...')
while True:
        #     Get the reading on just on channel, channel 0 is the first channel on the device.
    current_reading = mcp3428.take_single_recording(0)#channel 0 reading from adc
    end = time.time()#end timer
    time_interval = end - start#find duration of timer
    rate = (current_reading - previous_reading)/time_interval#math to find rate of voltage increase
    save_reading = current_reading
    
    print 'Channel 0 reading: '
    print current_reading
    print '\r\n'
    print 'Rate of Increase: '
    print rate
    print '\r\n'

    if (rate > 2):# change to a waiting period to leavel out the voltage after the current spike
        voltage -= 1
        bit = voltage/conversion_factor
        time.sleep(0.01)
        dac.set_voltage(bit)
        time.sleep(0.01)
    elif (previous_reading == current_reading):#this condition should be better, daniel!
        voltage += 1
        bit = voltage/conversion_factor
        time.sleep(0.01)
        dac.set_voltage(bit)
        time.sleep(0.01)

    start = time.time()
    time.sleep(1)
        
    
