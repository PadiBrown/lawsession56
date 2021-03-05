while True:
    try:
        gross = int(input("what is your gross salary?"))
        kids = int(input("how many children do you have?"))
    except ValueError:
        print("Enter numbers only")
#avoid cheaters
if kids > 10:
    kids = 10
#once here we have proper numbers
tax = 0
if gross < 1000:
    tax = 10
elif gross < 2000:
    tax = 14
else:
    # it means more or equal to 4000
    tax = 18
if gross < 2000:
    tax = tax - (kids*1)
else:
    tax = tax - (kids*0.5)
print("with a gross of", gross, "and", kids, "kids you take home",gross*(100-tax)/100)

