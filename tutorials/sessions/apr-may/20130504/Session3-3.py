# Program to accept input from keyboard. 
# Call function ValidateInput to perform the following checks
# The format of the input string should be
#    Input string should be 4 chracters
#    1st character is either U or L
#    2nd, 3rd and 4th characters are numeric and less than 255

# Import modules for serial, time and sys
import serial
import time
import sys



# Function to validate input string
def ValidateInput (StrToValidate):

	# If input string is not 4 character , print message and return False
	if len(StrToValidate) != 4:
		print "Command must be 4 characters"
		return False  
	
	# If 1st character is not U or L, print message and return False 
	if (StrToValidate[0] != "L") and (StrToValidate[0] != "U"):
		print "First character must be L or U"
		return False
	
	# If 2,3, & 4 character are not digits, print message and return False 
	if not ((StrToValidate[1] + StrToValidate[2] + StrToValidate[3]).isdigit()):
		print "Not Digits"
		return False
	

	# If 2,3, & 4 character are greater than 255, print message and return False 
	if int(StrToValidate[1] + StrToValidate[2] + StrToValidate[3]) > 255:
		print "character 2,3,4 must be less than 255"
		return False
	
	# After all validation checks have been run and passed return True
	return True



# Create and open the serial port, setting the communication rate
# For this to work properly, the speed you specify here needs to match exactly with the speed on the Arduino
# Note that not all values are possible ... look up the possible values for serial baud rate online

# Serial ports on Linux/Unix like machines have names like /dev/ttyXXXX
# Serial ports on Windows machines have names like COM3 or COM8
# Modify this to matcht the serial port that the Arduino is actually connected to

# serialport = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
# serialport = serial.Serial("COM3", 115200, timeout=0.5)
 serialport = serial.Serial('/dev/ttyACM0', 11520, timeout=0.5)

# Wait a 2 seconds, in case the arduino reboots on serial port opening.
time.sleep(2) # short pause in case arduino reboots on serial port opening, value can be changed or line removed


# Accept input from keyboard and store in RawInputCommand
RawInputCommand = raw_input("Please enter a command ")


# Call ValidateInput function and pass input string as parameter.
if ValidateInput(RawInputCommand):
	# All validation checks have been successful, print message
	print ("Input command is valid")


# In this example, we will make a binary string to send to the serial port
# This matches with a command receiver on our Arduino which expects to see a command string in a certain format
# Our standard simple format is <sync byte><length byte><command bytes>

# We use the Python "bytearray" to hold our string of bytes to send to the Arduino
# Our command is 4 bytes long:
# .. byte[0] 0xFC (a special marker indicating the start of the command)
# .. byte[1] 2 (the length: the number of bytes to come)
# .. byte[2] 'U' (the character U, which is a command that the Arduino understands
# .. byte[3] 0 (a "parameter" for the command U, which the Arduino understands

# commandValue holds the numeric parameter - characters 2,3,4 in input string
commandValue =int(RawInputCommand[1] + RawInputCommand[2] + RawInputCommand[3])


commandBuffer = bytearray()
commandBuffer.append(0xFC)
commandBuffer.append(2)
commandBuffer.append(ord(RawInputCommand[0]))
commandBuffer.append(commandValue)

serialport.write(commandBuffer) # write the command buffer

# In response to this command, the Arduino sends back a response.
# Just print it out. To really deal with this response, it should have a defined format, and we should process it to understand what it means

response = serialport.readlines(None) # reads from serial port
print(response) # outputs data received from serial port
		
