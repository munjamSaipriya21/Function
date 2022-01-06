import random
guessesTaken = 0
number = random.randint(1, 10)
print(' I am thinking of a number between 1 and 20:')
while guessesTaken < 5:
   guess = int(input( "eneter the guess number="))
 #print(number)
   # guessesTaken = guessesTaken + 1
   if guess < number:
 	   print('Your guess is too low,go higher.')
   
   # elif guess > number:
 	#    print('Your guess is too high go lower.')
   # elif guess == number:
 	#    print("you win this game ",number,"this is your correct number")
 	#    break
 	# print("you are coming out the game ")