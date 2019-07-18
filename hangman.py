import random

# A list of words that
potential_words = ["python", "pseudo", "jumble", "design", "create", "jazzed"]

word = random.choice(potential_words)

# Use to test your code:

# print(word)

# Converts the word to lowercase
word = word.lower()
alphabet = ["a b c d e f g h i j k l m n o p q r s t u v w x y z"]

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    if guess == word:
        print("You win!")
        break
    elif guess in word:
        print("Guessed right!")
        for let in range(len(word)):
            if word[let] == guess:
                print(word[let])
                current_word[let] = guess
    else:
        print("Guessed wrong")
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
    # check if the guess is valid: Is it one letter? Have they already guessed it?
    # check if the guess is correct: Is it in the word? If so, reveal the letters!
    print(current_word)

    if not "_" in current_word:
        print("You win!")
        break

print("You failed :(")

    #fails = fails+1
    #print("You have " + str(maxfails - fails) + " tries left!")
