""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

import os 
import sys
import datetime 

#Obro fitxer de lectura
fLab = open('arxiu73_words_002.lab', 'r')

ResList = [] #Llista resultant

AuxList = []*3 #Llista on es fa el processat de la subfrase

Linia = []

for lin in fLab:

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

        #print(ResList)

        AuxList = Linia[:]


print(ResList)
fLab.close()
