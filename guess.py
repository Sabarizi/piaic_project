import random

def main():
    # Generate the secret number at random!
    # random.randint() function ka use kiya gaya hai is kaam ke liye.
    secret_number: int = random.randint(1, 50 )
    
    print("I am thinking of a number between 1 and 50...")
    
    # Get user's guess 
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        if guess < secret_number:  # If-statement is True if guess is less than secret number
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print() # Print an empty line to tidy up the console for new guesses
        guess: int = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()
