import drugs
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

listofreports = drugs.get_reports()
# based on age group, how many people have been dependent on alcohol in the past year?

for f in listofreports:
    oldest_group = f["Totals"]["Alcohol"]["Dependence Past Year"]["26+"]
    mid_group = f["Totals"]["Alcohol"]["Dependence Past Year"]["18-25"]
    young_group = f["Totals"]["Alcohol"]["Dependence Past Year"]["12-17"]

objects = ['12-17 years old', '18-25 years old', '26+ years old']
x_pos = np.arange(len(objects))
values = [young_group, mid_group, oldest_group]
clr = '#F09D00'
labels = ['99', '400', '1200']

for i in range(len(x_pos)):
    plt.text(x = x_pos[i]-0.1, y = values[i], s = labels[i], size = 9)

plt.bar(x_pos, values, align='center', color=clr)
plt.xticks(x_pos, objects)
plt.ylabel('# of people (in thousands)')
plt.xlabel('age group')
plt.title('Alcoholism in the Past Year')
plt.show()
