""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')

ResList = [] #Llista resultant

AuxList = []*3 #Llista on es fa el processat de la subfrase

Linia = []

num_subt = 0

for lin in fLab:

  lin = lin.strip()

  Linia = lin.split(' ')

  if(Linia[2].isupper()): 

    if(len(AuxList) != 0):

      ResList.append(AuxList)
      
      AuxList = [] 

    ResList.append(Linia)


  else:

    if(len(AuxList) == 0):

      AuxList = Linia[:]

    else:

      if(len(AuxList[2] + Linia[2]) <= 35):

        AuxList[2] = AuxList[2] + Linia[2] 

        AuxList[1] = Linia[1]     

      else:

        ResList.append(AuxList)

        AuxList = Linia[:]

while num_subt < len(ResList):

  print(ResList[num_subt][0]," ",ResList[num_subt][1]," ",ResList[num_subt][2])

  num_subt += 1

fLab.close()
