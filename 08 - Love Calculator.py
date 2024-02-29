print("The Love calculator is calculatating your score ........")
name1 = input("Enter the name of first person : ")
name2 = input("Enter the name of second person: ")

combined_name = name1+name2
lower_name =  combined_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e
score = str(first_digit) + str(second_digit)

print(f"Your love score is {score}")