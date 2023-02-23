#lab3.23floor.py
#take in a float number and outputs an int that is rounded down
#author Kev Donovan

import math
number_to_floor = float(input("Enter a float number: "))
floored_number = math.floor(number_to_floor)
print(' {} floored is {}'.format(number_to_floor,floored_number))
