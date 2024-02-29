print("Welcome to Most Advance Roller Coster Ride")
height = int(input("Enter your height in cm: "))
bill = 0

if height >= 120:     
    print("You can ride the Rollercoster") 
    age = int(input("Enter your age: ")) #asking for user's age.
    if age < 12 :      
        bill = 5 #Determining the  cost of ticket for a child (age less than 12)
        print("You are child and Ticket price is $5")
    elif age <= 18 : 
        bill  = 7 #Determining the cost of ticket for a teenager (age between 12 and  18).
        print("You are Teenager. Ticket Price is $7")
    elif age >=45 and  age<=55: #Here, AND operator is used and this means that  both conditions should be true at the same time.
        print("Everything is going to be okay and you have a free ride on us. So, enjoy the ride.")
    else :   
        bill=12 #Determining the cost of ticket for an adult (age greater than 18).
        print("You are Adult. Ticket Price is $12")
    want_photoes  = input('Do you want photoes with your ticket?(y/n):')#Asking  whether they want photos or not.
    if want_photoes == "y":
        bill +=3
        print(f"You Want Extra Photoes Service. So Total cost of ticket is ${bill}")
else:             
    print("Sorry, you are too short. You cannot ride the Rollercoster.") 