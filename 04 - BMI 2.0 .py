weight = input ("Write  your weight in kg: ")
height = input("write your height in meters : ")
#Converting the inputs from string to float
weight=float(weight)
height=float(height)
BMI=(weight/(height**2))
if  BMI <18.5:
    print(f"Your BMI is  {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You have normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI} ,You are slightly overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI} ,You are obese")
else:
    print(f"Your BMI is {BMI}. You are overweight")