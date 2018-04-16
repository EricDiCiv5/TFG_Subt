""" Objectiu: Juntar frases de 35 caràcters dels fitxers .txt"""

#Importacions de llibreries i/o funcions
import os 
import sys
import glob

#Fitxer de lectura
fTXT = open("002_frases.txt", 'r')

#Variables
Subf = []


#Fitxers .txt en llista
for line in fTXT:
    
  if not (line.split(' ')[0].isupper()) and not (line.split(' ')[0].islower()) or (line.split(' ')[0].islower()):

    while len(line):

      if (len(line) > 35):
        subf_35 = line[0:35]
        subf = subf_35[:subf_35.rindex(' ')]
        Subf.append(subf)
        line = line[subf_35.rindex(' ')+1:]
   
      else:
      
        subf_35 = line[0:]
        subf = subf_35[:subf_35.rindex('\n')]
        Subf.append(subf)
        line = []

#Eliminar strings buits
Subf = list(filter(None, Subf))

#Visualització llista
print(Subf)

fTXT.close()
