""" Objectiu: Juntar frases de 35 caràcters dels fitxers .txt"""

#Importacions de llibreries i/o funcions
import os 
import sys
import glob

#Fitxer de lectura
Conj_fTXTs = glob.glob('./*.txt')

    
#Fitxers .txt en llista
for nom_fitx in Conj_fTXTs:
  fTXT = open(nom_fitx, 'r')
  fList = open(nom_fitx.replace('txt', 'srt'), 'w')

  #Variables
  Subf = []

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

  pos = 1

  #Visualització llista
  while pos  < len(Subf):
    fList.write(Subf[pos]+'\n')
    fList.write('')
    pos += 1

fTXT.close()
fList.close()
