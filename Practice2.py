print("Welcome to the rollercoaster! Height and age are required for price")
height = int(input("Enter your height in cm: "))
bill = 0
age = int(input("How old are you? "))

if height >= 120:
        print("You are tall enough!")
        if age <= 12:
                bill = 5
                print("Child tickets are $5")
        elif age <= 18:
                bill = 7
                print("Youth tickets are $7")
        elif age>= 45 and age <= 55:
                print("(have a free ride on us!)")
        else:
                bill = 11
                print("Adult tickets are $11")
        wants_photo = input("Would you like a photo? Type y or n")
        if wants_photo == "y":
                bill  += 3
        print(f"Your total is {bill}")
else:
        print("You are not tall enough to ride on your own and must be accompanied by an adult!")