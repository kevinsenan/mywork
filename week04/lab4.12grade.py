#lab4.2grade.py
#read a student's percentage mark and print out grade
#author Kevin Donovan

percentage = float(input("Enter a percentage: "))


if percentage < 0 or percentage > 100:

    print("Please enter a number between 0 and 100")
elif percentage < 40: 
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 1")
elif percentage < 70:
    print("Merit 2")
else:
    print("Distinction")
    
