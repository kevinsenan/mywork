#lab3.22absolute.py
#gives absolute value of a number ie a negative number is positive
#author Kev Donovan


#number is implied to be a float so input will be cast that way

number = float(input("Enter a number: "))
#get the number into cent
cent = number * 100
absolute_value = abs(cent)
print('The absolute value of {} is {}'.format(number, absolute_value))
