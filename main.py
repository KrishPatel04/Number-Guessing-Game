
#Number Guessing game
#Python Modules
from random import randint
from colorama import Fore, Back, Style
from time import sleep
import sys

#Text effect
def char_delay(text, delay):
  for letter in text:
    print(letter, end="")
    sleep(delay)
    sys.stdout.flush()



#Game background
char_delay(Fore.WHITE + "The two player number guessing game is desinged for two players to guess a random generated number between a certain range dependening on the mode difficulty.\nThis game will require two players, so go grab your friends!\n\n", 0.05)

#Initial score board & set up
score_1 = 0
score_2 = 0

play_again = True
while play_again == True:
  #Intro w/ user input for name
  p1_name = str(input(Fore.BLUE + Style.BRIGHT + "Player 1, enter your name." + Back.RESET + Style.DIM + " "))
  p1_name = p1_name.upper() #Capitalized for consistentcy
  
  p2_name = str(input(Style.RESET_ALL + Style.BRIGHT + Fore.CYAN + "Player 2, enter your name." + Back.RESET + Style.DIM + " "))
  p2_name = p2_name.upper() #Capitalized for consistentcy
  
  #Capitalized letters used to accept incorrect capitalization for players
  
  char_delay(Fore.MAGENTA + Style.RESET_ALL + "\nHello " + Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + " and " + Fore.CYAN + Style.BRIGHT + p2_name + Fore.RESET + Style.RESET_ALL + " and welcome to THE NUMBER GUESSING GAME❗❗", 0.04) #Greetings
  
  #Level of difficulty (LOD)
  char_delay("\n\nEnter the difficulty you would like to play.\n🟩 Easy: Guess between 1-10\n🟦 Medium: Guess between 1-100\n🟥 Hard: Guess between 1-1000\n\n", 0.03)
  LOD = input("What would you like? ")
  LOD = LOD.lower()
  
  #Make sure user input was correct:
  while True:
    if LOD == "easy": #If user selection is easy, random integer between 1 & 10.
      num_gen = randint(1, 10)
      break #Ends loop to prevent infinite looping!
    
    elif LOD == "medium": #Else if user selection is medium, random integer between 1 & 100.
      num_gen = randint(1, 100)
      break #Ends loop to prevent infinite looping!
    
    elif LOD == "hard": #Else if user selection is hard, random integer between 1 & 1000.
      num_gen = randint(1, 1000)
      break #Ends loop to prevent infinite looping!
    
    else: #Code takes into
      LOD = input("Invalid input.\nPlease try again. Remeber to only enter easy, medium, or hard: ") #Prompts user again to enter LOD. Code will then run again within the WHILE loop.
  
  #Number of rounds
  rounds = input("\n\nHow many rounds would you like to play to? ")
  
  while True:
    if rounds.isnumeric():
      char_delay("Perfect! There will be " + str(rounds) + " rounds of the " + LOD + " game mode.\n\n", 0.02)
      break
    
    else:
      rounds = input("\nInvalid input.\nPlease only enter a numerical value for the number of rounds you would like to play: ")
  
  rounds = int(rounds)
  while rounds > 0:
    guess_1 = int(input(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + ", pick a number:" + Fore.RESET + Style.RESET_ALL + " "))
    if guess_1 > num_gen:
      print("Incorrect. 😞\nEnter a lower value! 📉\n")
  
    elif guess_1 < num_gen:
      print("Incorrect. 😞\nEnter a higher value! 📈\n")
  
    elif guess_1 == num_gen:
      print("\nCorrect!! You get one point! 🙃")
      rounds = rounds - 1
      score_1 += 1
      print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_1) + " points!! 🤑\n" + Style.BRIGHT + Fore.CYAN + p2_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_2) + " points.\n")
  
      if rounds > 0:
        char_delay(Back.YELLOW + "NEW GAME, NEW NUMBER GENERATED!! 😄" + Fore.RESET + Style.RESET_ALL + Back.RESET, 0.02)
      if rounds == 0:
        break
        
      #RESTART
      if LOD == "easy": #If user selection is easy, random integer between 1 & 10.
        num_gen = randint(1, 10)
    
      elif LOD == "medium": #Else if user selection is medium, random integer between 1 & 100.
        num_gen = randint(1, 100)
      
      elif LOD == "hard": #Else if user selection is hard, random integer between 1 & 1000.
        num_gen = randint(1, 1000)
  
    if guess_1 != num_gen or guess_1 == num_gen:
     guess_2 = int(input(Style.BRIGHT + Fore.CYAN + p2_name + ", pick a number:" + Fore.RESET + Style.RESET_ALL + " "))
  
    if guess_2 > num_gen:
      print("Incorrect. 😞\nEnter a lower value! 📉\n")
  
    elif guess_2 < num_gen:
      print("Incorrect. 😞\nEnter a higher value! 📈\n")
  
    elif guess_2 == num_gen:
      print("\nCorrect!! You get one point! 🙃")
      rounds = rounds - 1
      score_2 += 1
      print(Fore.CYAN + Style.BRIGHT + p2_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_2) + " points!! 🤑\n" + Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_1) + " points.\n")
      if rounds > 0:
        char_delay(Back.YELLOW + "NEW GAME, NEW NUMBER GENERATED!! 😄" + Fore.RESET + Style.RESET_ALL + Back.RESET, 0.02)
  
      if rounds == 0:
        break
      #RESTART 2
      if LOD == "easy": #If user selection is easy, random integer between 1 & 10.
        num_gen = randint(1, 10)
    
      elif LOD == "medium": #Else if user selection is medium, random integer between 1 & 100.
        num_gen = randint(1, 100)
      
      elif LOD == "hard": #Else if user selection is hard, random integer between 1 & 1000.
        num_gen = randint(1, 1000)
  
  #GAME WINNER DETERMINATION
  char_delay("THE WINNER:\n", 0.07)
  
  if score_1 > score_2:
    print(Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_1) + " points, while " + Style.BRIGHT + Fore.CYAN + p2_name + Fore.RESET + Style.RESET_ALL + " only has " + str(score_2) + " points.\nThis means " + Fore.BLUE + Style.BRIGHT + p1_name.upper() + Fore.RESET + Style.RESET_ALL + " WINS!! 😎")
  if score_1 < score_2:
    print(Style.BRIGHT + Fore.CYAN + p2_name + Fore.RESET + Style.RESET_ALL + " has " + str(score_2) + " points, while " + Fore.BLUE + Style.BRIGHT + p1_name + Fore.RESET + Style.RESET_ALL + " only has " + str(score_1) + " points.\nThis means " + Style.BRIGHT + Fore.CYAN + p2_name.upper() + Fore.RESET + Style.RESET_ALL + " WINS!! 😎")
  
  char_delay("\n\nThank you for playing!\n", 0.05)
  
  play_again = input("Would you like to play? ")
  play_again = play_again.lower()
  
  if play_again == "yes" or play_again == "sure" or play_again == "yeah" or play_again == "okay" or play_again == "ok" or play_again == "ye" or play_again == "of course" or play_again == "ofc":
    play_again = True
    char_delay("\nYay 🤗\n\nNEW GAME\n", 0.03)
    continue
  else:
    play_again = False
    char_delay("\nNo worries! See you next time. 👋", 0.01)
    break
  
