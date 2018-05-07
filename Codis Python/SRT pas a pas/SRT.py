""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.txt'."""

#Importacions de llibreries i/o funcions
import os 
import sys
from functools import reduce
from collections import deque
import re
import glob
import string


#Funcions
def seg_a_temps(string):

  segons = float(string)

  return "%02d:%02d:%02d.%03d" % \
      reduce((lambda ll,b : divmod(ll[0],b) + ll[1:]),
          [(segons*1000,),1000,60,60])
"""
#Fitxers lectura
Conj_fLabs = glob.glob('./*.lab')
Conj_fTXTs = glob.glob('./*.txt')
for (nom_fitx, nom_fich) in zip(Conj_fLabs,Conj_fTXTs):
  fLab = open(nom_fitx, 'r')
  fTXT = open(nom_fich, 'r')
  fSRT = open(nom_fich.replace('txt', 'srt'), 'w')"""

fTXT = open('002_frases.txt', 'r')
fLab = open('arxiu73_words_002.lab', 'r')
fSRT = open('arxiu73_002.srt', 'w')

#Variables

Subf = [] #Llista fitxers text

AuxList = []*3 #Llista on es fa el processat de la subfrase

Labs = [] #Llista fitxers labels (etiquetes)

pos = 0 #comptador posició

#Fitxers .txt en llista
for line in fTXT:

  #si frase comença per lletra majúscula o minúscula...
  if not (line.split(' ')[0].isupper()) and not (line.split(' ')[0].islower()) or (line.split(' ')[0].islower()):

    while len(line):

      if (len(line) > 35):
            
        subf_35 = line[0:35]
        subf = subf_35[:subf_35.rindex(' ')] #Agafar subfrase fins l'últim espai dels 35
        Subf.append(subf)
        line = line[subf_35.rindex(' ')+1:] #Actualitzar valor línia

      else:
      
        subf_35 = line[0:]
        subf = subf_35[:subf_35.rindex('\n')] #Agafar subfrase fins el punt i part
        Subf.append(subf)
        line = [] #Actualitzar valor línia
        
#Eliminar strings buits
Subf = list(filter(None, Subf))


#Llegir .lab en llista partint línies
lines = fLab.read().splitlines()

#Fitxers .lab en llista
for phrase1 in Subf:

  #Indicador processat frase del fitxer '.lab'
  phrase2 = False
  
  if not (lines[pos].split(' ')[2].isupper()) and not (lines[pos].split(' ')[2].islower()) or (lines[pos].split(' ')[2].islower()):

    #Mentre frase no s'hagi fet o no estigui en la última línia...
    while not (pos == len(lines)-1):
    
      if(len(AuxList) == 0): #Si llista Auxiliar és buida...
        
        #Si primera paraula LABs igual a primera paraula TXTs...
        if(lines[pos].split(' ')[2] == phrase1.split(' ')[0]):

          #Copiar contingut llista Línia en Auxiliar
          AuxList = list(lines[pos])
          print(AuxList)
          #Actualitzar marca de temps final.
          AuxList[0] = lines[pos].split(' ')[0] 

          pos += 1
        
      else:
  
        #Si longitud subfrase més paraula es inferior a longitud frase del TXT...
        if(len(AuxList[2] + lines[pos].split(' ')[2]) <= len(phrase1)): 

          AuxList[2] = AuxList[2] + lines[pos].split(' ')[2] #Concatenació en AuxList.

          #Si darrera paraula LABs igual a darrera paraula TXTs...
          if(AuxList[2][-1] == phrase1.split(' ')[-1]):	
            
            AuxList[1] = lines[pos].split(' ')[1] #Agafar marca de temps final.
        
          pos += 1

        else:
          res = seg_a_temps(AuxList[0])+" "+seg_a_temps(AuxList[1])+" "+phrase1
          Labs.append(res)
          AuxList = []

print(Labs)

fTXT.close()
fLab.close()
fSRT.close()
