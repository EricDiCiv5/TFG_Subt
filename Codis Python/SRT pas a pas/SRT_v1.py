""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys
import datetime 

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')


for lin in fLab:

  i_time,f_time,word = lin.split(' ')

  print(i_time)

  print(f_time)

  print(word)

fLab.close()
