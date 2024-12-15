num = int(input("Enter the number that you want to enter:"))
if (num % 100 == 0) and (num % 400 == 0):
    print("{} is a leap year.".format(num))
elif (num % 4 == 0) and (num % 100 != 0):
    print("{} is a leap year.".format(num))
else:
    print("{} is not a leap year.".format(num))