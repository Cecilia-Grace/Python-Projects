import random

while True:
    user_input = input("Roll the dice(y/n)? ").lower()

    if user_input == "y":
        print(random.randint(1, 6), random.randint(1, 6))
        user_input 
    elif user_input == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid Choice!")