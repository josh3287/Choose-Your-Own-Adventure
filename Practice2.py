print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
        print("You are tall enough!")
        age = int(input("How old are you? "))
        if age <= 12:
                print("Please pay $5")
        elif age <= 18:
                print("Please pay $7")
        else:
                print("Please pay $11")
else:
        print("You are not tall enough to ride on your own and must be accompanied by an adult!")