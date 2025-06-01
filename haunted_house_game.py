print("Welcome to the Haunted House Game!")
answer1 = input("Which way would you like to go? (left/right):")
if answer1 == "left":
     print("You entered a dark room and there is a coffin there.")
     answer2 = input ("Will you open the coffin? (yes/no):")
     if answer2 == "yes":
            print("You found a ghost inside the coffin!Game over.")
     else:
           print("You decided not to open the coffin and runs away from the house.")
else:
     print("You entered a room where a weird looking cake is on the table.")
     answer3 = input("Will you eat the cake? (yes/no):")
     if answer3 == "yes":
            print("The cake was poisoned! Game over.")
     else:
           print("You decided not to eat the cake and found a way out of the house. You win!")
   