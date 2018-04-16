""" Objectiu: Generar fitxer '.SRT' partint del fitxers de paraules '.lab'."""

#Importacions de llibreries i/o funcions
import os 
import sys
from functools import reduce
import glob

#Funcions
def seg_a_temps(string):

  segons = float(string)

  return "%02d:%02d:%02d.%03d" % \
      reduce((lambda ll,b : divmod(ll[0],b) + ll[1:]),
          [(segons*1000,),1000,60,60])

#Fitxers lectura
Conj_fLabs = glob.glob('./*.lab')
Conj_fTXTs = glob.glob('./*.txt')


for nom_fitx in Conj_fLabs:
  fLab = open(nom_fitx, 'r')
  fSRT = open(nom_fitx.replace('lab', 'srt'), 'w') 

  
  #Variables
  Subf = []

  ResList = [] #Llista resultant

  AuxList = []*3 #Llista on es fa el processat de la subfrase

  Linia = [] #Llista on s'agafa cada linia del fitxer

  num_subt = 0 

  pos = 0 #Posició llista .txt (Subf)

  #Fitxers .lab en llista
  for lin in fLab:

    Linia = lin.split(' ') #Partir línia en els 3 paràmetres que la formen

    if not (Linia[2].isupper() and not Linia[2].islower()): #si la paraula comença per lletra majúscula...

      if(len(AuxList) == 0): #Si llista Auxiliar és buida...

        AuxList = Linia[:] #Copiar contingut llista Línia en Auxiliar

      else:

        if(len(AuxList[2] + Linia[2]) <= 35): #Si longitud subfrase més paraula es inferior a 35...

          AuxList[2] = AuxList[2] + Linia[2] #Juntar els strings en llista Auxiliar
          AuxList[1] = Linia[1] #Agafar marca de temps final     

        else:

          ResList.append(AuxList) 
          AuxList = Linia[:] 


  ResList.append(AuxList)


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

  
  #Comparar llista '.lab' amb '.txt'
  for num_subt in ResList:

    while(len(Subf):

      if (Subf[pos] == ResList[num_subt][2]): 

        ResList[num_subt][2] = Subf[pos]  


  #Emmagatzematge del format pels fitxers .SRT
  while num_subt < len(ResList):

    fSRT.write(str(num_subt+1)+'\n')
    fSRT.write(seg_a_temps(ResList[num_subt][0])+" --> "+seg_a_temps(ResList[num_subt][1])+'\n')
    fSRT.write(' '.join(ResList[num_subt][2].split())+'\n')
    fSRT.write('\n')

    num_subt += 1

fLab.close()
fTXT.close()
fSRT.close()
