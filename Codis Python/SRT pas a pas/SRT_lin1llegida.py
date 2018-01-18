""" Objectiu: printar per pantalla cada línia llegida del fitxer "002_frases.txt"."""

import os 
import sys 

num_subt = 1 #Contador del número de subtítol

#Obro fitxers de text de lectura
f1 = open('002_frases.txt', 'r') 

for lin1 in f1:

  print(lin1)

f1.close()
