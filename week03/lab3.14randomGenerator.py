#lab3.4randomGenerator.py
#print out a random number, the user inputs the start number and the end number for the range
#author Kevin Donovan

import random

x = int(input("Enter number: "))
y = int(input("Enter the range: "))

number = random.randint(x,y)
print("here is the random number: {} ".format(number))
