
# file: voltage_ramp.py
# brief: Sets ramp for the High Voltage Supply

import time
import random
import Adafruit_MCP4725
import mcp3428
import smbus
import numpy as np

# create bus object
bus = smbus.SMBus(1)
# create a dictionary of addresses and information needed for the ADC instance
kwargs = {'address': 0x68, 'mode': 0x10, 'sample_rate': 0x08, 'gain':0x00}

# crate a ADC instance
mcp3428 = mcp3428.MCP3428(bus, kwargs)

# Create a DAC instance, initializing the class in this file
# the dac variable names correspond to the addresses to the dac's in DECIMAL, while the
# address given in the actual call for the MCP4725 class is in HEXADECIMAL

#Voltage Dac
dac96 = Adafruit_MCP4725.MCP4725(address=0x60, busnum=1)

#Max Current Dac
dac97 = Adafruit_MCP4725.MCP4725(address=0x61, busnum=1)


def voltage_ramp(goalVoltage):
    
    bitVoltage = 0
    bitCurrent = 4095
    
    convVolt = 0.0025156
    convCurr = 0.0023887

    voltageConversion = 300
    
    
    # set the voltage to zero. Since the DAC recieves a voltage in bits,
    # and is twelve bits (12 bits), the range
    # we can set these to are between 0 and 4095 for voltages that range from 0 V to 10 V.
    print('------------')
    print('Voltage set to 0 V...')
    print('------------')
    print('Max Current Set to 3.3 mA')
    print('------------')
    
    dac96.set_voltage(bitVoltage)
    dac97.set_voltage(bitCurrent)   
    
    # start timer: we need timers to regulate the rate at which the high voltage is incremented
    
    prevTime = time.time()

    #begin while loop of increments and decrements
    while 1:
        # read the voltage at the beginning of each iteration.
        # these readings are from 0 to 10 V, so convert wisel

        #get the livetime and what until 1 second passes
        livetime = time.time()
        if livetime-prevTime < 2:
            continue

        voltageReading = mcp3428.take_single_reading(0)
        voltage = voltageReading * voltageConversion

        currentReading = mcp3428.take_single_reading(1)
        
        #resets the prevTime variable for the next increment
        prevTime = livetime
        print('-----------------------------')        
        print('voltage (0 to 3000 V): ' + str(voltage))
        print('-----------------------------')
        print('max current (0 to 10 V): ' + str(currentReading))
        print('-----------------------------')
                
        if voltage < goalVoltage:
            bitVoltage += 1
            print('bit: ' + str(bitVoltage))
            print('-----------------------------')
            dac96.set_voltage(bitVoltage)
        else:
            hold_value(goalVoltage, bitVoltage)


def hold_value(goalVoltage, bitVoltage):
    print('Holding at ' + str(goalVoltage) + 'Volts.....')
    while 1:
        voltageReading = mcp3428.take_single_reading(0)
        voltage = voltageReading * voltageConversion
        
        if voltage < (goalVoltage - 2):
            bitVoltage += 1
            dac96.set_voltage(bitVoltage)
        elif voltage > (goalVoltage + 2):
            bitvoltage -= 1
            dac96.set_voltage(bitVoltage)
        else:
            continue
        
#reset the parameters of the ramp below, then run the function voltage_ramp.exe
if __name__ == '__main__':
    print('Voltage Ramp')
    print('\r\n')
    goalVoltage = int(input('Enter high voltage amount: '))
    voltage_ramp(goalVoltage)
