# Note: if u're on replit, u have to: from replit import clear instead of line 3
# then use: clear() wherever u want
import random
from os import system
from art import logo


def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards."""
  # note:
  # we have two returns, if the first one runs, it escapes from the function
  # otherwise the second return works
  # note 2: if it's a blackjack, has to escape from the function
  if sum(cards) == 21 and len(cards) == 2:
    # 0 represent a blackjack in our game
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compare scores between two values."""
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
  
  # variables
  # Note: u have to define these variable inside of this function, otherwise ur program won't work
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  # _ because we don't need this particular variable
  # we need for this loop to run twice
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    # End the game
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

# when the user is done, it's computer's turn
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

# print the result
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

# Ask user to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
  system('clear')
  play_game()