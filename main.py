import random
from replit import clear
from art import logo

def deal_card():
  #assumption that each card has an equal chance of occuring
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):

  if 11 in cards and 10 in cards and len(cards) == 2: 
  #a simplified way would be sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(your_score, computer_score):

  if your_score > 21 and computer_score > 21:
    return "Bust! You lose 👎"

  if your_score == computer_score:
    return "Draw 😒"
  elif computer_score == 0:
    return "You lose! Opponent has Blackjack 😱"
  elif your_score == 0:
    return "You win! You have a Blackjack 😉"
  elif your_score > 21:
    return "Bust. You lose 👎"
  elif computer_score > 21:
    return "Opponent bust! You win 🏆"
  elif your_score > computer_score:
    return "You win 🏆"
  else:
    return "You lose 👎"

def play_game():

  print(logo)
  your_cards = []
  computer_cards = []
  game_over = False

  for _ in range(2):
    your_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_over:

    your_score = calculate_score(your_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {your_cards}, current score: {your_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if your_score == 0 or computer_score == 0 or your_score > 21:
      game_over = True
    else:
      you_should_deal = input("Type 'y' for another card, type 'n' to pass: ")
      if you_should_deal == "y":
        your_cards.append(deal_card())
      else:
        game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {your_cards}, final score: {your_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(your_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
