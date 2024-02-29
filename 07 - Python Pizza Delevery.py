print("Welcome to Python Pizza Delevery.")
size = input("Enter the size of pizza you want:S, M or L : ")
add_pepperoni =  input ("Do you want add pepperoni? Y/N: ")
extra_cheese =  input("Do you want extra cheese? Y/N: ")
bill = 0 #This is created to keep track of the bill
if size == "S":
    bill += 15
elif  size == "M" :
    bill +=20
else:
    bill += 25
    
if add_pepperoni == "y":
    if size == "S":
       bill +=2
    else:
           bill+=3
else:
    bill  +=0
    
if extra_cheese == "y":
    if  size == 'S':
       bill +=1
    else:
        bill +=3
else:
    bill  +=0  
print(f"Your total bill is $ {bill}.")