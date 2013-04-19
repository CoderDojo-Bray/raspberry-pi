# Simple code snippet to write to & read from RPi serial port
# CoderDojo Bray April 2013


# Requires PySerial API which is included in standard Raspbian image
# If installation required
# see http://pyserial.sourceforge.net/pyserial.html
# or try 'sudo apt-get install python-serial' on RPi

import serial   # imports serial module
import time     # imports time module
serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)  # opens port - change name of serial port if not standard port on RPi, change baud rate as required, change timepout as required
time.sleep(2)   # short pause in case arduino reboots on serial port opening, value can be changed or line removed
serialport.write("STRING TO SEND TO SERIAL PORT")    # write string/data, to serial - change value as required
response = serialport.readlines(None)   # reads from serial port
print response    # outputs data received from serial port


# Notes
# Tested on QEMU emulator, not a real RPi
# Front end required to generate string to send to serial
# Back end required to interpret output from serial port
