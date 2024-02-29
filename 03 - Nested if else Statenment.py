print("Welcome to Advance version of RollerCoster!!")
height = int(input("Enter your height in cm: "))

if height >= 120:     
    print("You can ride the Rollercoster") 
    age = int(input("Enter your age: ")) #asking for user's age.
    if age < 12 :      #If user is a child (less than 12 years) then he/she will pay $5.
        print("You are child and Ticket price is $5")
    elif age <= 18 : #If user is a teenager equal to 18 years, then he/she will pay $7.
        print("You are Teenager. Ticket Price is $7")
    else :   #For adults , They should have to pay $12.
        print("You are Adult. Ticket Price is $12")

else:             
    print("Sorry, you are too short. You cannot ride the Rollercoster.") 