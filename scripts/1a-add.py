#!/bin/env python

# title: 1a-add.py
# description: Fais une addition de 2 nombres
# date: 15/10/2018
# author: Axel PARIS

# ------------------------
#
#        Imports
#
# ------------------------

import re

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

# Add function
def add(n1, n2):
  return n1 + n2

# ------------------------
#
#       Variables
#
# ------------------------

number1 = input('Entrez un nombre: ')
number2 = input('Entrez un autre nombre: ')


# ------------------------
#
#          Script
#
# ------------------------

if not is_number(number1) or not is_number(number2):
  print('Oups ! Vous devez entrer des nombres')
  exit()

print(add(number1, number2))