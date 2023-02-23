# O(1) Time Complexity

def even_or_odd(number):
    if (number % 2) == 0:
        return True
    else:
        return False
print(even_or_odd(13))

# O(n) Time Complexity

def less_than_100(list_of_numbers):
    for number in list_of_numbers:
        if number > 99:
            return False    
    return True
print(less_than_100([1, 2, 3, 4, 14]))



def repeated_names(list_of_names):
    for name in list_of_names:
        is_duplicate = False
        while is_duplicate == False:
            if name == name:
                is_duplicate = True
    return is_duplicate


print(repeated_names(["Gavin", "Brittany", "Gwen", "Sonja", "Modi", "Meena", "Modi"]))