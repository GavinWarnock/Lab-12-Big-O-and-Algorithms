def even_or_odd():
    number = int(input("What number would you like to check "))
    if (number % 2) == 0:
        return True
    else:
        return False
print(even_or_odd())