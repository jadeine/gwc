a = [2, 3, 4, 5, 6, 7, 8, 9]
e = ["egg", "flour", "dew"]

a.extend(e)
print(a)

b = a[1:4]
print(b)
# starts at the first index (3), and ends at the fourth (5). the fourth index is not included.

c = a[1:4:2]
print(c)
# the number after the second colon (2) indicates increments.

d = a[::-1]
print(d)
# the negative number sorts the list into reverse.
