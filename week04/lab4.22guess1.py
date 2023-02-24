#lab4.22guess1.py
#prompt user to enter number until they get it right
#author Kev Donovan

number_to_guess = 30

guess = int(input("Please guess the number: "))
while guess != number_to_guess:
    print("Wrong")
    guess = int(input("Please guess again "))

print("well done! Yes the number was ", number_to_guess)
