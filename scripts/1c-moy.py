#!/bin/env python

# title: 1c-moy.py
# description: Afficher une liste de prenoms donne par un utilisateur
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

notes = {}
firstname = ""
nbTopNotes = 5
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
  if not is_number(value):
    if re.match(firstname_pattern, value) is None:
      return False
    else:
      return True
  else:
    return False

# Get notes average
def get_note_average(notes):
  totalSum = 0
  total = 0
  for firstname in notes :
    totalSum += notes[firstname]
    total += 1
  avg = totalSum / total
  return avg

# Get top 5 notes
def get_top_notes(notes):
  topNotes = []
  # Calculating top 5 notes
  for firstname in notes :
    topNotes.append(notes[firstname])

  # Sort notes reversing
  topNotes.sort(reverse=True)
  return topNotes

# Display top notes
def display_top_notes(topNotes, nbTopNotes):
  for note in topNotes :
    if(nbTopNotes >= 0): 
      print(note)
    else:
      break
    nbTopNotes -= 1

# ------------------------
#
#          Script
#
# ------------------------

# While user wants to add a new firstname and his note
while firstname != "q":
  firstname = input('Entrez un prenom: ')

  # Check if user input is correctly formated
  if is_firstname(firstname):
    if (firstname == "q"):
      break
    
    note = ''
    while not is_number(note):
      note = input('Saisir la note de '+ firstname +': ')
      if is_number(note):
        notes[firstname] = note
      else:
        print('Vous devez entrez une note (nombre)')
  else:
    print('Vous devez entrez une chaine de caracteres valide (sans espace)')


# Calculating and displaying the average
avg = get_note_average(notes)
print("Moyenne des notes:")
print(avg)

# Getting and diplaying top 5 notes
topNotes = get_top_notes(notes)
print("Top 5 des meilleures notes:")
display_top_notes(topNotes, nbTopNotes)