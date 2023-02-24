#lab4.24topthree.py
#generat 10 random numbers print out the top 3.
#author Kev Donovan

import random
how_many = 10
top_how_many = 3
range_from = 0
range_to = 100

#create an empty array called numbers
numbers = []

#loop for 0 to 10 times and append the random numbers generated in range 0 to 100
for i in range(0,how_many):
    numbers.append(random.randint(range_from,range_to))
#print 10 for number of random numbers, space with a tab and print the array numbers
print (f"{how_many} random numbers\t {numbers}")

#copy the array of numbers into top_ones
top_ones = numbers.copy()

#sort the numbers
top_ones.sort(reverse = True)

#print the top number in the variable top_how_many
print (f"The top {top_how_many} are \t\t {top_ones[0:top_how_many]}")