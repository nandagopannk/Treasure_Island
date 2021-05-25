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

print("Welcome to the Treasure Island!!!\n")
name = input("What is your Name???\n")
print("Dear " + name + " Your mission is to find the treasure!!!!\n")

print("\n")

choice1 = input('Dear '+ name + ' You\'re at across road. Where do you want to go??? Type "left" or "right" \n').lower()

print("\n")

if choice1 == "right":
  print("While you are crossing the road you have a car has hit you.... You are dead.... Game Over... :-)\n")
if choice1 == "left":

  choice2 = input('Dear ' + name + ' You\'ve come to a big lake... There is an island in the middle of the lake... Type "wait" for the boat or "swim" to swim across. :-) \n').lower()

  print("\n")

  if (choice2) == "swim":
    print("While you're swimming you have been eaten by the shark.... You are dead... Game Over.... :-(\n")
  if choice2 == "wait":

    choice3 = input('Dear ' + name +' You have arrive at the island unharmed.... There is an house with three doors. One "red", one "yellow" and one "blue". Which colour would you choose??? :-) \n').lower()

    print("\n")

    if choice3 == "red":
      print("Its an room full of fire... You are dead... Game Over :-( \n")
    if choice3 == "yellow":
        print("Dear" + name + "Youve a got a room full of money and gold..... You won..... Congratulations.... Don\'t forget to share your money with me... :-)\n")
    if choice3 == "blue":
      print("You have reached in a room of low temprature..... You have become an ice... You are dead... Game Ove... :-(\n") 

      print("\n")

      input("dear " + name + " How well do you rate your experince with us... In a scale of 0-10\n")

      print("_______________________________________________")
      
