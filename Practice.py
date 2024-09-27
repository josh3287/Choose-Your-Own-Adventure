print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm: "))

if height >= 120:
        print("You are tall enough!")
        age = int(input("How old are you? "))
        if age >= 18:
              print("You meet the requirements. Enjoy the ride!")
        elif age < 18:
              print("Sorry, you must be accompanied by an adult")
else:
    print("Sorry, you are not tall enough!")