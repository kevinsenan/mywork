#lab3.3div.py
#read in two numbers , divide first by second and give integer result and the remainder
# author Kev Donovan

x = int(input("Enter the first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x / y)
print(answer)

remainder = x%y
print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))