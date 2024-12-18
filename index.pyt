
import random

# Define symbols for the slot machine
symbols = ['🐾','🐰','🐇','🦄','🐣''🦜']

# Define payout multipliers for each symbol (this can be adjusted)
payouts = {
    '🐾': 15, 
    '🐰': 30,
    '🐇': 8,
    '🦄': 50,
    '🐣': 20,
   '🦜': 10,
}

# Function to simulate the spinning of three reels
def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

# Function to calculate winnings based on the reel result
def calculate_winnings(reel_result, bet_amount):
    # Check if two or more symbols match
    unique_symbols = set(reel_result)
    if len(unique_symbols) == 1:  # All three symbols match
        return bet_amount * payouts[reel_result[0]]
    elif len(unique_symbols) == 2:  # Two symbols match
        return bet_amount * 2  # Double the bet for two matching symbols
    else:
        return 0  # No match

# Function to handle the slot machine game
def play_slot_machine():
    balance = 1000  # Starting balance
    
    print("Welcome to the Spin and Win Machine!")
    print(f"Your starting balance is: ₹{balance}")
    
    # Loop to allow multiple spins
    while balance > 0:
        # Ask the player to enter their bet amount
        bet_amount = float(input(f"\nEnter your bet amount (Current balance: ₹{balance}): "))
        
        # Validate bet amount
        if bet_amount <= 0 or bet_amount > balance:
            print("Invalid bet amount! Please bet within your balance.")
            continue
        
        # Spin the reels and display the result
        print("Spinning the reels...")
        reel_result = spin_reels()
        print(f"Reel result: {reel_result}")
        
        # Calculate winnings
        winnings = calculate_winnings(reel_result, bet_amount)

        # Update balance
        balance += winnings - bet_amount

        # Display the result
        if winnings > 0:
            print(f"Congratulations! You won ₹{winnings}!")
        else:
            print("Sorry, for your loss.")

        print(f"Your current balance is: ₹{balance}")

        # Ask if the player wants to continue playing
        if balance > 0:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        else:
            print("You ran out of money! Thanks for playing!")
            break

    print(f"Your final balance is: ₹{balance}")

# Run the slot machine game
if __name__ == "__main__":
    play_slot_machine()
