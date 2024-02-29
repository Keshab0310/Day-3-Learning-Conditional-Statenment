print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input("In Which direction you want to go? Left or Right: ").lower()
if choice1 == "left":
    choice2 = input("Now you have reached the river and the island is in the middle of lake and you have two choices, Do you want to swim or wait: ").lower()
    if choice2 == "wait":
        choice3 = input("You have found the boat and travelled the island via boat and You have landed the island safely......... But there are three doors to choose and which color do you prefer to choose? Red, White or Green?: ").lower()
        if choice3 == "red":
            print("There was monster hiding beside thhat door. Haha You have died.")
        elif choice3 == "white":
            print("You found a room filled with snakes. You are not able to survibe this........ You are dead")
        elif choice3 == "green":
            print("You have found the Treasure....... Congratulation!!")
        else:
            print("This door is not available, So monster had found you  and killed you.")
    else:
        print("Haha, You don't know how to swim, So you have died.")
else:
    print("You are travelling wrong direction and bandits had attacked you... so you are dead")
