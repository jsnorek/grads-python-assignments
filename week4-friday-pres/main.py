import random # Importing the random module to generate random choices for the computer choice

# Function to get the user's choice
def get_user_choice():
    while True: # Infinite loop asking for user input until a valid choice is made
        try: # try block to catch any ValueErrors
            # Ask user to enter their choice 
            user_choice = input("Enter your choice! (rock, paper, or scissors): ").strip().lower() # For input, gets rid of whitespace and coverts to lowercase
            # Error handling for invalid user input
            if user_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError("Invalid choice. Please try again and choose 'rock', 'paper', or 'scissors'.")
            return user_choice # Return the valid user choice
        # If error flagged, print the error
        except ValueError as e:
            print(e) # Print error message

# Function for getting the computer's random choice
def get_computer_choice():
    # Return a random choice from the list
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    # Check if user and computer choices are the same
    if user_choice == computer_choice:
        # Return tie if choices are the same
        return "It's a draw!" 
    # Else If statement to check for user winning conditions
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        # Return user wins message
        return (f"You win! {user_choice} beats {computer_choice}")
    else: # If none of the above conditions are met
        # Return computer wins message
        return (f"Computer wins with {computer_choice}!")

# Main function to run the game    
def main():
    # Print welcome to game message
    print("It's time to play!")
    # Infinite loop to keep game running until user decides to stop
    while True:
        # Get the user's choice
        user_choice = get_user_choice()
        # Get the computer's choice 
        computer_choice = get_computer_choice()
        # Print computer's choice
        print(f"Computer chose: {computer_choice}")
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        # Print the results
        print(result)

        # Prompt user to play again or not
        play_again = input("Do you want to play again? (yes/no): ").strip().lower() # For input, gets rid of whitespace and coverts to lowercase
        # Alternative line for only accepting "yes" input from user to restart the game
        # if play_again != 'yes':
        if play_again not in ['yes', 'y']:
            # Print goodbye message
            print("Thanks for playing!")
            # Exit loop and end the game
            break

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function to start the game
    main()