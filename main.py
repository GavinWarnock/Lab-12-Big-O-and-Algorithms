# O(1) Time Complexity

def even_or_odd(number):
    if (number % 2) == 0:
        return True
    else:
        return False
print(even_or_odd(13))



def less_than_100(list_of_numbers):
    for number in list_of_numbers:
        if number > 100:
            return False
        else:
            return True
print(less_than_100([1, 2, 3, 4, 500]))

