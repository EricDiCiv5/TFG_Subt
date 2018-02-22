""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys
import datetime 

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')

SubtList =  []

num_subt = 1

i = 0

for lin in fLab:

  SubtList.append(lin.split(' '))

  print(SubtList[i][0])

  print(SubtList[i][1])

  print(SubtList[i][2])

  i += 1

fLab.close()
