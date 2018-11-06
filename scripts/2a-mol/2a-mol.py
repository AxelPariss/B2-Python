#!/bin/env python3.6

# title: 2a-mol.py
# description: Jeu du plus ou moins qui lit & ecrit dans un fichier
# date: 23/10/2018
# last edited: 04/11/2018
# author: Axel PARIS

# ------------------------
#
#        Imports
#
# ------------------------

import random
import time

# ------------------------
#
#       Variables
#
# ------------------------

file_path = "jeu.txt"
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
    write_in_file('Oups ! Vous n\'etes pas alle au bout :/')
  else :
    write_in_file('Bravo !')

# clean file
def clean_file():
  file = open(file_path, "w")
  file.write('')
  file.close()

# Write in file
def write_in_file(text):
  # Read last content
  content = read_in_file()
  
  # Write last + new contenr
  file = open(file_path, "w")
  file.write(content + text)
  file.close()

# Read in file
def read_in_file():
  file = open(file_path, "r")
  input = file.read()
  file.close()
  return input

# Read last line in file
def read_last_line_file():
  file = open(file_path, "r")
  input = file.readlines()
  file.close()
  if input:
    return input[-1]
  else:
    return ''

# Check if value is a number
def is_number(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

# ------------------------
#
#          Script
#
# ------------------------

clean_file()
write_in_file("Bienvenue dans el famoso jeu du plus ou moins !\nEntrez un nombre compris entre "+str(min_value)+" et "+str(max_value)+"\n")

# While the user doesn't found the random number
while win == False :
  user_input = read_last_line_file()

  # We wait user submit a value
  if not is_number(user_input):
    time.sleep(1)
  elif int(user_input) > random:
    write_in_file('Trop grand !\n')
  elif int(user_input) < random:
    write_in_file('Trop petit !\n')
  else:
    win = True

# Print final message
if win == True:
  display_result(random)
else:
  display_result()

