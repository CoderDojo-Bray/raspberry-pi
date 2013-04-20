# Simple code snippet to write to & read from serial port
# You can use this as an example for how to make a proper program to communicate with something on a serial port
# Like, for instance, an Arduino

# CoderDojo Bray April 2013
# Copyleft Shaun Thorpe 2013

# Mods Liam Friel 2013

# Requires PySerial API to be installed
# see http://pyserial.sourceforge.net/pyserial.html
# or try 'sudo apt-get install python-serial' on RPi/Linux
# or install from source on Windows

# This is not a finished program. How to improve:

# .. make the command sending code into a function
# .. make a loop to send several commands
# .. accept commands from the user on the keyboard, and translate these into commands for the Arduino

# Super advanced:
# .. monitor the data coming back from the Arduino using a thread
# .. send sensor data coming back from the Arduino to Scratch over the network


import serial   # imports serial module
import time     # imports time module

# Create and open the serial port, setting the communication rate
# For this to work properly, the speed you specify here needs to match exactly with the speed on the Arduino
# Note that not all values are possible ... look up the possible values for serial baud rate online

# Serial ports on Linux/Unix like machines have names like /dev/ttyXXXX
# Serial ports on Windows machines have names like COM3 or COM8
# Modify this to matcht the serial port that the Arduino is actually connected to

# serialport = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)  
serialport = serial.Serial("COM3", 115200, timeout=0.5)  

# Wait a 2 seconds, in case the arduino reboots on serial port opening.

time.sleep(2)   # short pause in case arduino reboots on serial port opening, value can be changed or line removed

# In this example, we will make a binary string to send to the serial port
# This matches with a command receiver on our Arduino which expects to see a command string in a certain format
# Our standard simple format is <sync byte><length byte><command bytes>

# We use the Python "bytearray" to hold our string of bytes to send to the Arduino
# Our command is 4 bytes long:
# .. byte[0] 0xFC  (a special marker indicating the start of the command)
# .. byte[1] 2     (the length: the number of bytes to come)
# .. byte[2] 'U'   (the character U, which is a command that the Arduino understands
# .. byte[3] 0     (a "parameter" for the command U, which the Arduino understands

commandBuffer = bytearray()
commandBuffer.append(0xFC)
commandBuffer.append(2)
commandBuffer.append(ord('U'))
commandBuffer.append(0)

serialport.write(commandBuffer)    # write the command buffer

# In response to this command, the Arduino sends back a response.
# Just print it out. To really deal with this response, it should have a defined format, and we should process it to understand what it means

response = serialport.readlines(None)   # reads from serial port
print(response)    						# outputs data received from serial port



