import random
from game_data import data
from art import logo, vs
import os

correct = 0

def start():

  person_a = random.choice(data)
  play(person_a, correct)

def play(person_a,correct):

  print(logo)

  if correct >= 1:
    print(f"You have {correct} correct!")

  print(f"Compare A: {person_a['name']}, {person_a['description']} from {person_a['country']}")
  
  print(vs)
  
  person_b = random.choice(data)
  while person_b == person_a:
    person_b = random.choice(data)

  print(f"Compare B: {person_b['name']}, {person_b['description']} from {person_b['country']}")
  
  answer = input("Who has more followers? Type 'A' or 'B':").lower()
  
  a = person_a['follower_count']
  b = person_b['follower_count']

  if a > b and answer == "a": 
    correct += 1
    os.system('cls')
    play(person_a, correct)
  elif b > a and answer == "b":
    correct += 1
    os.system('cls')
    play(person_b, correct)
  else:
    game_over(correct)

def game_over(correct):
  play_again = input(f"Sorry! You lose!! You got {correct} correct! Want to play again? 'Y' for Yes. 'N' for No").lower()
  if play_again == "y":
    start()
  else:
    print("Thanks for playing! See you again soon!")
    exit()

start()