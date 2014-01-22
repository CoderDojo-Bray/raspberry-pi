# SerialRead.py

# Import libraries
import serial
import sys

# X will be used as loop counter
x = 1

# InChar will be used to hold value from serial port
InChar = 0

# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)

# Flush contents of serial port
ser.flush()

# Loop while x is less than 10
while x < 10:

	# Read value from serial port
	InChar = ser.readline()
			
	# Print loop counter x and value read from serial port
	print x, InChar

	# Increment x by 1
	x = x + 1

# Close serial port
ser.close

