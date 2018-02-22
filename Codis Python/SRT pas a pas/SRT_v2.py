""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys
import datetime 

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')

SubtList = []

i = 0

for lin in fLab:

  i_time,f_time,word = lin.split(' ')

  SubtList.append(lin)

  print(SubtList[i])

  i += 1

fLab.close()
