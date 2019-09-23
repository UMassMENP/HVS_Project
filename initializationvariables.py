import time 

previous_reading = 0
current_reading = 0
conversion_factor = .002 #How the readings change when they get read into and out of the ADC
voltage = 0
dac.set_voltage(0) #set the voltage to zero through the dac instance
set_voltage = True
start = time.time() #start the timer to step up the Voltage
previous_reading = mcp3428.take_single_recording(0)
