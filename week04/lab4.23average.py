#lab4.23average
#prompt user to enter a number and when thye hit 0 show the average of all the numbers
#author Kev Donovan


# declare numbers as an empty array
numbers = []

#number stores the value the user enters
number = int(input("Enter a number (0 to quit): "))

#check the user didn't enter 0, if not add the value in number to the array
while number != 0:
    numbers.append(number)
#ask the user for another number
    number = int(input("Enter another number (0 to quit): "))

for value in numbers:
       print(value)

average = float(sum(numbers)) / len(numbers)
print(f"The average is {average}")
