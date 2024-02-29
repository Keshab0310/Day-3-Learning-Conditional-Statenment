print("Welcome to Leap Year Calculator")
year = input(input("Enter a year: "))
year1 = int (year)
if (year1 % 4 == 0):
    if (year1 % 100 == 0):
        if (year1 % 400 == 0):
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a  leap year.")
else:
    print(f"The year {year} is not a leap year.")