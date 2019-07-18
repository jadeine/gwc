#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
sides = ["fries", "mashed potatoes", "mac & cheese", "salad", "baked potatoes"]
entrees = ["steak", "smoked salmon", "filet mignon", "short rib", "burger"]
desserts = ["ice cream", "chocolate lava cake", "brownies", "cheesecake", "cookies"]

#Generates a random integer.
chosenside = randint(0, len(sides)-1)
chosenentree = randint(0, len(entrees)-1)
chosendessert = randint(0, len(desserts)-1)

print(entrees[chosenentree], "as your main dish with a side of", sides[chosenside], "and", desserts[chosendessert], "for dessert!")
