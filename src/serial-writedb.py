# Simple program to read values from the serial port and insert them into a database table
# Look at the code: what else does it do?

# Uses a MySQL database: assumes this is installed already and that the credentials match what is hardcoded 
import serial
import time
import MySQLdb as mdb

import sys

x = 1
InChar = 0
HighLow = ""

ser = serial.Serial('/dev/ttyACM0', 9600)

con = mdb.connect('localhost', 'testuser', 'test623', 'test');

cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS \
#        RndNums(Id INT PRIMARY KEY AUTO_INCREMENT, RNum Int)")


ser.flush()

while x < 10:
	InChar = ser.readline()
			
	if int(InChar) > 50:
		HighLow = "High"
		ser.write(chr(0x1))
	else:
		HighLow = "Low"
		ser.write(chr(0x0))
		
	print x, HighLow, InChar
	cur.execute("INSERT INTO RndNums(RNum) VALUES('" + str(InChar) + "')")
	x =x + 1

cur.execute("Commit;")	
ser.close



    
    
