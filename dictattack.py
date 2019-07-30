#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
testpw = test_password.lower()

#Write logic to see if the password is in the dictionary file below here:
for line in f:
    if testpw == line.strip():
        print("Your password is too weak!")
        break
    if len(testpw) < 6:
        print("Your password is too short!")
        break
    if len(testpw) > 16:
        print("Your password is too long!")
        break
    if testpw == testpw.replace('a', '4'):
        print("Your password is too weak!")
        break
    if testpw == testpw.replace('s', '5'):
        print("Your password is too weak!")
        break
    if testpw == testpw.replace('t', '7'):
        print("Your password is too weak!")
        break
    if testpw == testpw.replace('o', '0'):
        print("Your password is too weak!")
        break
    if testpw == testpw.replace('l', '1'):
        print("Your password is too weak!")
        break
    if testpw == line + '2019':
        print("Your password is too weak!")
        break
    else:
        print("Your password is valid!")
        break
