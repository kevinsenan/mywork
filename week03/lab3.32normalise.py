#lab3.24normalise.py
#read a stringremove leading or trailing spaces and convert to lower case. Also sow lengths of both
#author Kev Donovan

raw_string = input("Please enter a string: ")

normalised_string = raw_string.strip().lower()

length_of_raw_string = len(raw_string)
length_of_normalised = len(normalised_string)

print(f"That string normalised is: {normalised_string}")
print(f"We reduced the input string from {length_of_raw_string} to {length_of_normalised} characters")
