choice1 = input('Welcome to Treasure Island! Your mission is to find the treasure. You\'re at a crossroad. Type left or right: ').lower()

if choice1 == "left":
    choice2 = input("You made it past the trap! You've arrived at a lake, do you want to swim or wait?: ").lower()
    if choice2 == "wait":
        choice3 = input("A boat has arrived and have made it to the building. Choose a red or blue door: ").lower()
        if choice3 == "blue":
            print("You win!")
else:
    print("You fell into a hole. Game over")