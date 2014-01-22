from random import randint


# Generate random number between 1 and 10
RandomNum = randint(1,10)

# Keep track of the number of guesses
NumGuesses = 1

# Allow user 5 guesses
while NumGuesses < 5:
	Guess = int(raw_input("Please enter your guess "))
	
	if Guess == RandomNum:
		print "Correct guess"
	elif Guess < RandomNum:
		print "You guessed too low"
	else:
		print "You guessed too high"
		
	NumGuesses = NumGuesses + 1
			
