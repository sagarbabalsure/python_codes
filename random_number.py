import string
import random
from random import randint
x = randint(1, 100)
count=3
while count>0:
	y=int(input("Enter your guess: "))
	count=count-1
	if x==y:
		print("Oh..your guess is correct")
	else:
		print("you have %d guesses remaining" %count)

if count==0:
	print("sorry you lose")
else:
	print("congrats")

def randomstring(size):
	return ''.join(random.sample(char,size))

char=string.letters+string.digits+string.punctuation
print(char)
print("random string is: %s" %(randomstring(randint(6,10))))