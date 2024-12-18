
import random

symbols = ['🐾','🐰','🐇','🦄','🐣','🦜']

payoff = {
    '🐾': 15, 
    '🐰': 30,
    '🐇': 8,
    '🦄': 50,
    '🐣': 20,
   '🦜': 10,
}

def spin_reels():
    return [random.choice(symbols) for _ in range(3)]

def calculate_winnings(reel_result, bet_amount):
    unique_symbols = set(reel_result)
    if len(unique_symbols) == 1:  
        return bet_amount * payoff[reel_result[0]]
    elif len(unique_symbols) == 2:  
        return bet_amount * 2  
    else:
        return 0  


def play_slot_machine():
    balance = 1000  
    
    print("Welcome to the Spin and Win Machine!")
    print(f"Your starting balance is: ₹{balance}")
    
    while balance > 0:

        bet_amount = float(input(f"\nEnter your bet amount (Current balance: ₹{balance}): "))
        
       
        if bet_amount <= 0 or bet_amount > balance:
            print("Invalid bet amount! Please bet within your balance.")
            continue
        
       
        print("Spinning the reels...")
        reel_result = spin_reels()
        print(f"Reel result: {reel_result}")
        
       
        winnings = calculate_winnings(reel_result, bet_amount)

        balance += winnings - bet_amount
       
        if winnings > 0:
            print(f"Congratulations! You won ₹{winnings}!")
        else:
            print("Sorry, for your loss.")

        print(f"Your current balance is: ₹{balance}")

       
        if balance > 0:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        else:
            print("You ran out of money! Thanks for playing!")
            break

    print(f"Your final balance is: ₹{balance}")


if __name__ == "__main__":
    play_slot_machine()
