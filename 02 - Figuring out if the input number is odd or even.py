print("It is Odd and Even number detector")
number = input(f"Enter a number: ")
num = int(number)
if num % 2 == 0: # if the remainder of the division by 2 equals to zero, then it's an even number.
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")