import random

def high_low_game(rounds=5):
    score = 0  # Initialize player's score
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        
        # Generate random numbers for player and computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        # Show player's number
        print(f"Your number is: {player_number}")
        
        # Get player's guess (higher or lower)
        guess = input("Do you think your number is 'higher' or 'lower' than the computer's number? ").strip().lower()

        # Validate guess input
        while guess not in ["higher", "lower"]:
            guess = input("Invalid input! Please type 'higher' or 'lower': ").strip().lower()

        # Check the actual comparison
        if (guess == "higher" and player_number > computer_number) or \
           (guess == "lower" and player_number < computer_number):
            print(f"Correct! The computer's number was {computer_number}.")
            score += 1  # Player earns a point
        else:
            print(f"Wrong! The computer's number was {computer_number}.")
        
    # Display final score
    print(f"\nGame Over! Your final score is: {score}/{rounds}")

# Run the High-Low game
high_low_game()
