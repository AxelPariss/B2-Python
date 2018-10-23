#!/bin/env python

# title: 1d-dic.py
# description: Afficher une liste de prenoms donne par l utilisateur
# date: 15/10/2018
# last edited: 23/10/2018
# author: Axel PARIS


# ------------------------
#
#        Imports
#
# ------------------------

import re


# ------------------------
#
#       Variables
#
# ------------------------

firstnames = []
firstname = ""
firstname_pattern = r"^[a-zA-Z]+$"

# ------------------------
#
#       Functions
#
# ------------------------

# Check if value is a number
def is_number(value):
  try:
    int(value)
    return True
  except ValueError:
    return False


# Check if value is a correct string
def is_firstname(value):
  print(re.match(firstname_pattern, value))
  if not is_number(value):
    if re.match(firstname_pattern, value) is None:
      return False
    else:
      return True
  else:
    return False


# ------------------------
#
#          Script
#
# ------------------------

# While user wants to add a new firstname
while firstname != "q":
  firstname = input('Entrez un prenom: ')
  if is_firstname(firstname):
    if firstname != "q":
      # Add firstname to our list
      firstnames.append(firstname)
  else:
    print('Vous devez entrez une chaine de caractere valide (sans espace)')

# Sort firstnames in alphabetical order
firstnames.sort()

# Display firstnames
print(firstnames)