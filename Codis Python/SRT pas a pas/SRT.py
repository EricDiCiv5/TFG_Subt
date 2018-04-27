""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.txt'."""

#Importacions de llibreries i/o funcions
import os 
import sys
from functools import reduce
from collections import deque
import re
import glob

#Funcions
def seg_a_temps(string):

  segons = float(string)

  return "%02d:%02d:%02d.%03d" % \
      reduce((lambda ll,b : divmod(ll[0],b) + ll[1:]),
          [(segons*1000,),1000,60,60])

"""#Fitxers lectura
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
Subf = []

Marques = []

Labs = []*3

pos = 0

num_subt = 0

ini_t = ""

fin_t = ""

#Fitxers .txt en llista
for line in fTXT:

  #si frase comença per lletra majúscula o minúscula...
  if not (line.split(' ')[0].isupper()) and not (line.split(' ')[0].islower()) or (line.split(' ')[0].islower()):

    while len(line):

      if (len(line) > 35):
            
        subf_35 = line[0:35] #Agafar 35 caràcters
        subf = subf_35[:subf_35.rindex(' ')] #Agafar subfrase fins l'últim espai dels 35
        Subf.append(subf)
        line = line[subf_35.rindex(' ')+1:] #Actualitzar valor línia

      else:
      
        subf_35 = line[0:]
        subf = subf_35[:subf_35.rindex('\n')] #Agafar subfrase fins el punt i part
        Subf.append(subf)
        line = []
        
#Eliminar strings buits
Subf = list(filter(None, Subf))

#Fitxers .lab en llista
for lin in fLab:

  lin = lin.replace("\n","")

  if not (lin.split(' ')[2].isupper()) and not (lin.split(' ')[2].islower()) or (lin.split(' ')[2].islower()):
    Labs.append(lin.split(' ')) #Partir línia en els 3 paràmetres que la formen


#Eliminar strings buits
Labs = list(filter(None, Labs))


#Marques temps en .txt
for phrase in Subf:

  while pos < len(Labs):

    if(Labs[pos][2] == re.findall(r"[\S]+", phrase.split(' ')[-1])) or (Labs[pos][2] == phrase.split(' ')[-1]):
    
      ini_t = str(seg_a_temps(Labs[pos][1]))
      Marques.append(ini_t)  

    if(Labs[pos][2] == re.findall(r"[\S]+", phrase.split(' ')[0])) or (Labs[pos][2] == phrase.split(' ')[0]):

      fin_t = str(seg_a_temps(Labs[pos][0]))
      Marques.append(fin_t)

    pos += 1
 
#Format fitxer .SRT
while num_subt < len(Subf):

  fSRT.write(str(num_subt+1)+'\n')
  fSRT.write(ini_t+" --> "+fin_t+'\n')
  fSRT.write(Subf[num_subt]+'\n')
  fSRT.write('\n')

  num_subt += 1

fLab.close()
fTXT.close()
fSRT.close()
