import random

players = []
user_guesses = []

user_range_max = int(input("Enter maximum value: "))
user_range_min = int(input("Enter minimum value: "))
secret_number = random.randint(user_range_min, user_range_max)

number_of_players = int(input("How many players: "))
for i in range(number_of_players):
    user_name = input("Name: ").lower()
    players.append(user_name)
    i +=1
print(f"The players are: {players}")

player_scores = {user_name: 0 for user_name in players}
            
while True:
    try:
        if number_of_players == 1:
            user_guess = int(input(f"{user_name}: Guess the number between {user_range_min} and {user_range_max}: "))
        elif number_of_players > 1:
            user_name = input(f"Whose turn is it ({players}): ")
            user_guess = int(input(f"{user_name}: Guess the number between {user_range_min} and {user_range_max}: "))
   
        if user_guess:
            guesses = 1
        user_guesses.append(guesses)
      
        if user_guess == secret_number:
            print(f"Congratulations! Number was guessed in {len(user_guesses)} attempt(s).")
            player_scores[user_name.lower()] +=1
            for user_name, score in player_scores.items():
                print(f"{user_name}: Your score is: {score}")
            break          
        elif user_guess > secret_number:
            print("Too high!")           
        elif user_guess < secret_number:
            print("Too low!")  
        
                    
    except ValueError:
        print("Please enter a valid number")

