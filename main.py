# First, import the logo from art.py using the from/import syntax
from art import logo

# Next we will import the rest of the modules that will be used int his project
import os
import random

# There is not a command in VS code to clear the console when we want, so this is a work around
# Using the os module we imported above, we will create the follow function
def clear():
    """Clears the console across operating systems"""
    command = 'clear'
    # If statement to check to see what OS the computer is running. The "clear" command in windows is "cls", so if the computer is running windows it changes the command so it works
    if os.name == 'nt':
        command = 'cls'
    # inputs the command variable into the system function from the os module, this executes the command in the console/terminal
    os.system(command)
    
# Function to "pull a card" or deal from the deck at random
def deal_card():
    """Returns a random card from the deck"""
    # Create a card list for each card, ace through king
    # Note all royalty cards are 10
    # note enter ace as 11, rules state is can also be 1 but we will take care of that later
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # Use the random module with the choice method passing in the card list as set it to a variable
    card = random.choice(cards)
    return card

# Function to score our cards that are pulled from the deck
def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    # Create an if statement to check to see if a player has a blackjack hand (2 cards, an ace and a 10)
    if sum(cards) == 21 and len(cards) == 2:
        # Return 0 to represent our blackjack hand, we will use this instead of 21 to differentiate it from the normal score of 21
        return 0
    # Create an if statement that says if 11 is in the cards, and the sum is more than 21 change 11 to 1 so as not to bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Create a function that compares the score and returns an outcome
def compare(user_score, computer_score):
    """Pass in both the user's score and the computer's score as arguments"""
    # if/elif/else statements for each outcome
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with blackjack! WOOOOO!"
    elif user_score > 21:
        return "you went over. You lose :("
    elif computer_score > 21:
        return "you Win. opponent busted :)👃"
    elif user_score > computer_score:
        return "You win! 😊"
    else:
        return "You LOSE BOOOOOOO"

# Create game function
def play_game():
    """This function will be run so the game begins"""
    print(logo)
    
    # Create empty lists for user's and computer's cards, this is where the cards drawn by each "player" will be stored and how each of the above functions will make their calculations
    user_cards = []
    computer_cards = []
    # create a variable to notate weather the game should continue and use a boolean value of false
    is_game_over = False
    # Blackjack starts with 2 cards being dealt so we need to start the game with two cards being added to the user_cards and computer_cards list
    # use a for loop using the built in range() function to run the loop only twice
    for _ in range(2):
        # Use the append method with each empty list and pass in our deal_card function
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        # using the caluclate_score() function, create two new variables to store the scores by passing in our list as arguments
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Using print statements and F-strings, have the current score of the user and the first card of the computer's hand display
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}\n")
        
        # Create an if/else statement that states if either player has a blackjack hand or the user goes over 21 the game ends

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True # Ends the game loop
        else:
            # Create an input stored to a variable that asks the user to "hit" or "stand"
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to stand: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Create a while loop outside of our main game loop that keeps the computer playing as well as its score is not equal to 0 and under 17
    while computer_score != 0 and computer_score < 17:
        # Within this while loop we will have a card dealt to the computer, and score updated and stored to the computer_score variable
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    # Have print statements and F-strings that print out the final users score and computer score
    print(f"Your final hand: {user_cards}, you final score: {user_score}")
    print(f"Computers final hand: {computer_cards}, computers final score: {computer_score}")

    print(compare(user_score, computer_score))
    
# One final while loop that takes the user's input to start or leave the program, this also will be the first thing that will show when the program is run

while input('Want to play blackjack? type "y" to start, hit enter to leave: '):
    clear()
    play_game()