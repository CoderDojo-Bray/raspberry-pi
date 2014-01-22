# Program to accept input from keyboard. 
# The format of the input string should be
#    Input string should be 4 chracters
#    1st character is either U or L
#    2nd, 3rd and 4th characters are numeric and less than 255

# Import modules for serial, time and sys
import serial
import time
import sys


		
# Define variable to determine if input string is valid or not.
# Initially set this to True. It may be set to False during the validation checks
# InputStrValid = True

# Accept input from keyboard and store in RawInputCommand
RawInputCommand = raw_input("Please enter a command ")

# Validate the input string.
# If input string is not 4 character then print message and exit
if len(RawInputCommand) != 4:
		print "Input command must be 4 characters"
		exit(0)

		
# Check that 1st character is either U or L
# You need to write the code for this check


# Check that characters 2,3,4 are digits
# You need to write the code for this check


# Check that characters 2,3,4 are less than 255
# You need to write the code for this check



# All validation checks have been successful, print message
print ("Input command is valid")
		

