# SerialDB.py

# Import libraries
import serial
import time
import MySQLdb as mdb
import sys


# X will be used as loop counter
x = 1

# InChar will be used to hold value from serial port
InChar = 0

# HighLow set to High or Low depending on value in InChar
HighLow = ""


# Open serial port
ser = serial.Serial('/dev/ttyACM0', 9600)

# Flush contents of serial port
ser.flush()

# Open connection to MySQL database, User is testuser, 
# password is test623 and table is test
con = mdb.connect('localhost', 'testuser', 'test623', 'test');

# Create cursor to hold data to be written to database
cur = con.cursor()


# Loop while x is less than 10
while x < 10:

	# Read value from serial port
	InChar = ser.readline()

	# Check if value is greater than 50			
	if int(InChar) > 50:
		# Value > 50, set HighLow to High and
		# write a 1 to serial port
		HighLow = "High"
		ser.write(chr(0x1))
	else:
		# Value < 50, set HighLow to Low and
		# write a 0 to serial port
		HighLow = "Low"
		ser.write(chr(0x0))
		
	# Print loop counter x, Highlow and value
	# read from serial port
	print x, HighLow, InChar


	# Execute SQL statement to insert InChar value into
	# the RNUM column in the RndNums table 
	cur.execute("INSERT INTO RndNums(RNum) VALUES('" + str(InChar) + "')")


	# Increment x by 1
	x = x + 1

# Execute the SQL statement to commit/write data to
# database table. Without a Commit, data is not permanently
# stored in database
cur.execute("Commit;")	

# Close serial port
ser.close
 
