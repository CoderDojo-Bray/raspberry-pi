

	
def IsPrime (NumToCheck):
	
	# y is loop counter variable
	y=2.0
	
	while y < NumToCheck-1:
		
		if (NumToCheck/y) == int(NumToCheck/y):
			return False
			
		y = y +1
	
	return True



InputNumber = int(raw_input("Please enter number to check "))

if IsPrime(int(InputNumber)):
	print InputNumber, " is a prime"
	


InputNumber = int(raw_input("Please enter a number "))

# x is loop counter variable
x=1
while x <= InputNumber:
	if IsPrime(x):
		print x, " is a prime"
		
	x = x + 1
	

