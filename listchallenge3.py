list = [5, 3, 7, 1, 8]
list2 = [2, 4, 6, 9]

#challenge1 ----------------

#max = max(list)
#print(max)

#or -----

#list.sort()
#list.pop()
#print(list)

#challenge2 ----------------

#product = 1
#for i in list:
    #product *= i
#print(product)

#challenge3 ----------------

list.extend(list2)
list.sort()
a = list[::2]
print(a)
