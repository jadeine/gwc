import json

# create empty dictionary
#survey_ans = {}

# list of survey ques
survey_ques = [
    "what is your name?",
    "how old are you?",
    "do you put milk or cereal first?",
    "what app do you use most frequently?",
    "at what time do you usually sleep?",
    "what music genre do you listen to the most?",
    ]

# list of related keys
keys = ["name", "age", "milk/cereal", "color", "app", "bedtime", "music"]

# loop thru list of survey ques and take user input for responses
allUsers = []

done = "no"
while done == "no":
    survey_ans = {}
    i = 0
    for q in survey_ques:
        user_input = input(q + " ")
        survey_ans[keys[i]] = user_input
        i += 1
    allUsers.append(survey_ans)
    done = input("are you done collecting information? (yes or no): ")

# print dictionary
print(allUsers)

# attempt to read file
with open('survey2.json') as f:
    try:
        oldData = json.load(f)
    except ValueError:
        oldData = []
allUsers.extend(oldData)
f.close()

# write (w) to file
f = open("survey2.json", "w")
json.dump(allUsers, f)
f.close()

# milk or cereal first? stats
count = 0
milkCount = 0
cerealCount = 0
for d in allUsers:
    count += 1
    ans = d["milk/cereal"]
    if ans == "milk":
        milkCount += 1
    else:
        cerealCount += 1
if milkCount > cerealCount:
    print(str(milkCount) + " out of " + str(count) + " people put milk first!")
else:
    print(str(cerealCount) + " out of " + str(count) + " people put cereal first!")
