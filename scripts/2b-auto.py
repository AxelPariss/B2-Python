#!/bin/env python3.6

# title: 2b-mol.py
# description: Resolution du jeu du plus ou moins qui lit & ecrit dans un fichier
# date: 06/11/2018
# author: Axel PARIS

# ------------------------
#
#        Imports
#
# ------------------------

import time

# ------------------------
#
#       Variables
#
# ------------------------

file_path = "2a-mol/jeu.txt"
win = False
min_value = 0
max_value = 100
proposition = 0

# ------------------------
#
#       Functions
#
# ------------------------

# Print the result
def display_result():
    print('Bravo ! Le nombre était :' str(proposition))

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

# Get proposition
def get_proposition(less = None):
  if less == None:
    prop = (max_value - min_value) / 2 + min_value
  elif less == True: # If we need a less value
    prop = (proposition - min_value) / 2 + min_value
  else:
    prop = (max_value - proposition) / 2 + proposition
  return int(prop)

# Write correclt formatted proposition
def write_proposition():
  write_in_file(str(proposition)+'\n')

# ------------------------
#
#          Script
#
# ------------------------


proposition = get_proposition()
write_proposition()

# While the user doesn't found the random number
while win == False :
  result = read_last_line_file()
  print("Le script propose: "+ str(proposition) + '\n')

  # We wait user submit a value
  if result == 'Bravo !':
    win = True
  elif result == 'Trop grand !\n':
    print("Oups c'est trop grand...")
    proposition = get_proposition(True)
    write_proposition()
  elif result == 'Trop petit !\n':
    print("Oups c'est trop petit...")
    proposition = get_proposition(False)
    write_proposition()
  time.sleep(1.1)

# Print final message
display_result()
exit()
