# --- Define your functions below! ---

def intro():
    print("hello! i am the nicest chatbot around. <3")

def process_input(answer):
    if is_valid_input(answer):
        say_greeting()
    else:
        say_default()

def is_valid_input(greet):
    valid = ["hi", "hello", "hey", "yo", "heyo", "sup"]
    if greet in valid:
        return True
    else:
        return False

def joke_ans(word):
    right = ["burger-ndy", "burgerndy"]
    if word in right:
        return True
    else:
        return False

def say_greeting():
    print("hi!! how are you? are you doing GOOD, SO-SO, or BAD?")
    hru()

def hru():
    answer = input("(What will you say?) ")
    if answer == "good":
        hru_good()
    elif answer == "so-so":
        hru_soso()
    elif answer == "bad":
        hru_bad()
    else:
        print("what did you say? i didn't get that :(")
        hru()

def hru_good():
    print("that's great! me too, now that i'm talking to you. :) would you like a reminder? YES or NO?")
    answer = input("(What will you say?) ")
    if answer == "yes":
        print("try not to stay up too late tonight!")
        print("my creator slept at 3am last night and is highkey regretting it lmaoo don't be like her")
        print("i hope the rest of your day is great tho! bye!")
    elif answer == "no":
        print("that's ok! bye!")

def hru_soso():
    print("only so-so? :( every day should be great!")
    print("would you like me to tell you a joke to brighten your day?")
    answer = input("(What will you say?) ")
    if answer == "yes":
        print("what color are hamburgers?")
        answer = input("(What will you say?) ")
        if answer == "what":
            print("burger-ndy!")
            print("i hope i brightened your day with how bad this joke was! goodbye :)")
        elif joke_ans(answer):
            print("..learn how to play along with jokes lmao")
            print("have a great rest of your day anyway!")
    elif answer == "no":
        print("who Wouldn't want to hear a joke...")
        print("have a good rest of your day anyway!")

def hru_bad():
    print("oh no :( do you need some advice? YES or NO?")
    answer = input("(What will you say?) ")
    if answer == "yes":
        print("running away from your problems doesn't solve anything.")
        print("i may only be a computer, but i'll be here for you!")
        print("i hope the rest of your day is great!")
    elif answer == "no":
        print("that's ok! i hope you feel better soon. bye!")

def say_default():
    print("you're not gonna say hi? :( try again.")
    answer = input("(What will you say?) ")
    process_input(answer)

# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)
        break
        #print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
