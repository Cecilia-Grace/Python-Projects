import random

choices = ("r", "p", "s")
computer_choice = random.choice(choices)

emojis ={"r" : "🪨", "s" : "✂️", "p" : "📄"}
rounds = []
rounds_limit = 3
computer_score = []
user_score = []

user_name = input("What's your name: ")

while True:
        user_choice = input("Rock, paper, scissors(r/p/s): ").lower()
        rounds.append(1)
        
        if user_choice not in choices:
            print("Invalid choice!")
            continue
    
        print(f"You chose {emojis[user_choice]}")
        print(f"Computer chose {emojis[computer_choice]}")
                
        if user_choice == computer_choice:
            print("It's a tie ")
        elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
            print("You win")
            user_score.append(1)
        elif (user_choice == "r" and computer_choice == "p") or (user_choice == "p" and computer_choice == "s") or (user_choice == "s" and computer_choice == "r"):
            print("You lose")
            computer_score.append(1)
        
        if len(rounds) == rounds_limit:
                print("Game Over!")
                if len(computer_score) < len(user_score):
                    print(f"{user_name} won with a score of: {len(user_score)}")
                elif len(computer_score) > len(user_score):
                    print(f"Computer won with a score of: {len(computer_score)}")
                elif len(computer_score) == len(user_score):
                    print(f"You, {user_name} have tied with the computer ")  
                break
             
        proceed = input("Continue? (y/n) ").lower()
        if proceed == "y":
            user_choice
        elif proceed == "n":
            print("Goodbye!")
            break
   
