#!/bin/env python

# title: 1d-moy.py
# description: Jeu du plus ou moins
# date: 23/10/2018
# author: Axel PARIS

# ------------------------
#
#        Imports
#
# ------------------------
import random
import signal



# ------------------------
#
#       Variables
#
# ------------------------

win = False
min_value = 0
max_value = 100
random = random.randint(min_value, max_value)
user_input = ''


# ------------------------
#
#       Functions
#
# ------------------------

# Print the result
def display_result(result = None):
  if result is None:
    print('Oups ! Vous n\'etes pas alle au bout :/')
  else :
    print('Bravo ! Vous avez trouve, il s\'agit du nombre: '+str(result))

# Handle exiting game
def exit_game(sig, frame):
  print('\nAu revoir ;)')
  exit()



# ------------------------
#
#          Script
#
# ------------------------

# If the user press CTRL + C
signal.signal(signal.SIGINT, exit_game)

# While the user doesn't found the random number
while win == False :
  user_input = input('Entrez un nombre compris entre '+str(min_value)+' et '+str(max_value)+' : ')
  if user_input == 'q':
    break
  if int(user_input) > random:
    print('Votre proposition est trop grande !')
  elif int(user_input) < random:
    print('Votre proposition est trop petite !')
  else:
    win = True

# Print final message
if win == True:
  display_result(random)
else:
  display_result()

