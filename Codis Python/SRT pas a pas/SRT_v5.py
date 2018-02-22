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

  if(SubtList[i][2].isupper()):

    print(SubtList[i][2])

  else:

    while len(SubtList[i][2]) < 35:

      SubtList[i-1][2] = SubtList[i-1][2] + " " + SubtList[i][2]

      SubtList[i].clear()
    
  i += 1

fLab.close()
