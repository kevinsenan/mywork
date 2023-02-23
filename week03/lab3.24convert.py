#lab3.24convert.py
#take in float number and convert an absolut amount in int
#author Kev Donovan

import math
#number is implied to be a float so input will be cast that way

number = float(input("Please enter an amount: "))
#make the number positive
absolute_value = abs(number)
#change the absolute value to cents by mult by 100
convert = (absolute_value*100)
#round it to get rid of the decimal point
cent = int(round(convert))

print('That amount in cent is {}'.format(cent))