import random

rolls = []
while True:
    user_input = input("Roll the dice(y/n)? ").lower()
    
    if user_input == "y":
        rolls.append(1)
        numbers_of_dice = int(input("How many dice do you want to roll? "))
        print(f"You chose {numbers_of_dice} dice.")
        for i in range(numbers_of_dice):
            print(f"You rolled and got: {random.randint(1, 6)}")
            i +=1
            user_input 
    elif user_input == "n":
        print(f"You have rolled the dice: {len(rolls)} time(s).")
        print("Thanks for playing!") 
        break
    else:
        print("Invalid Choice!")
        
    
                    
                
        

        
         
