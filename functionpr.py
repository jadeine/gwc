def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def calc_total(list):
    #add all of the numbers in the list
    return sum(list)

print(is_even(7))
print(calc_total([1,2,3,4]))
