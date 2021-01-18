import random
print ("Winning rules of the game areas follows: \n" + " Rock vs scissor - Rock win \n" +
       "Scissor vs Paper - Scissor win \n" + "Paper vs Rock - Paper win" )
while True:
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor")
    choice= int(input("Choice of User"))
    while choice > 3 or choice < 1:
        print("Invalid Input")
    if choice == 1:
        name_of_choice= "Rock"
    elif choice == 2:
        name_of_choice= "Paper"
    else:
        name_of_choice= "Scissor"

print("Users choice is"+ name_of_choice)
print("Opponents turn now...")
while comp_choice == choice:
    comp_choice = random.randint(1,3)

if comp_choice == 1:
    comp_choice_name = "Rock"
elif comp_choice == 2:
    comp_choice_name = "Paper"
else:
    comp_choice_name = "Scissor"

print("Opponents choice is" + comp_choice_name)
print(name_of_choice + "v/s" + comp_choice_name)

if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
    print("Paper wins \n")
    result = "Paper wins"
elif ((choice == 3 and comp_choice == 1) or (choice == 1 and comp_choice ==3)):
    print("Rock wins \n")
    result = "Rock wins"
else:
    print("Scissor wins \n")
    result = "Scissor wins"

if result == name_of_choice:
    print ("Congratulations, User wins the game")
elif ((result == name_of_choice) and (result == comp_choice_name)):
    print ("Hey, Its a draw")
else:
    print("Oops! Opponent wins the game")

print("Do you want to play again? (Yes- Y or No- N)")
ans = input()
if ans == 'n' or ans =='N':
    break
print("Thanks forp playing")