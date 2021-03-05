try:
    # first we read the age as characters
    age = input("How old are you?")
    # we try to convert the age into a number
    age = int(age)
    7/0
except ValueError:
    print("Sorry, but that was not a number")
except ZeroDivisionError:
    print("Can't divide by zero)")
else:
    print("you were born around", 2021-age)
finally:
    print("Thanks for paying my game")