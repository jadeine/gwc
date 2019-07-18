#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
fruits = ["cherry", "orange", "jackfruit", "strawberry", "pineapple", "apple", "plum", "durian"]

#Generates a random integer.
aRandomIndex = randint(0, len(fruits)-1)
print(fruits[aRandomIndex])
