
# Update this text to match your story.
start = '''
One day, Christopher Robin and Pooh were bored.
They had to make a decision on whether to go to the park or have a tea party.
'''

print(start)

print("Type 'park' to go to the park or 'tea party' to have a tea party.") # Update to match your story.
user_input = input()
if user_input == "park":
    print("They decide to go to the park and meet Piglet there. Pooh asks Piglet if he wants to join their soccer match. Piglet agrees and they have an intense match. Pooh breaks Christopher Robin's ankles. After they finish, Christopher Robin asks Pooh if he wants to nap or have a tea party.") # Update to match your story.
    print("Type 'nap' to go back home and sleep or 'tea party' to have a tea party.")
    user_input = input()
    if user_input == "nap":
        print("The trio goes back home and decides to have a pillow fight. Piglet ended up with a bloody nose, so they all stopped and had a sleepover in Pooh's room.")
    elif user_input == "tea party":
        print("They choose to have a tea party and meet Rabbit, who joins them. Rabbit spills the tea about his neighbors. Pooh hypes him up to go say something to their faces. After they are all satisfied, Christopher Robin asks Pooh if he wants to go nap or to the jungle.")
        user_input = input()
        if user_input == "nap":
            print("The trio goes back home and watch movies until midnight. They decide to have a sleepover in Pooh's room.")
        elif user_input == "jungle":
            print("Christopher Robin and Pooh go to the jungle and play tag with Tigger. Tigger gets lost. Because it was too dark to look for him, Christopher Robin and Pooh give up on finding him for the day and will search for him tomorrow.")

    # Continue code to finish story.

elif user_input == "tea party":
    print("They choose to have a tea party and meet Rabbit, who joins them. After they are all satisfied, Christopher Robin asks Pooh if he wants to go nap or to the jungle.")
    print("Type 'nap' to go back home and sleep or 'jungle' to go to the jungle.")
    user_input = input()
    if user_input == "nap":
        print("The trio goes back home and decides to have a pillow fight. Piglet ended up with a bloody nose, so they all stopped and had a sleepover in Pooh's room.")
    elif user_input == "jungle":
        print("Christopher Robin and Pooh go to the jungle and play tag with Tigger. Tigger gets lost. Because it was too dark to look for him, Christopher Robin and Pooh give up on finding him for the day and will search for him tomorrow.")

    # Continue code to finish story
