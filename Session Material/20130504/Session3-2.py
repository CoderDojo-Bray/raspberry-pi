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



		
# Define variable to determine if input string is valid or not.
# Initially set this to True. It may be set to False during the validation checks
# InputStrValid = True

# Accept input from keyboard and store in RawInputCommand
RawInputCommand = raw_input("Please enter a command ")


# Call ValidateInput function and pass input string as parameter.

if ValidateInput(RawInputCommand):
	# All validation checks have been successful, print message
	print ("Input command is valid")
		
