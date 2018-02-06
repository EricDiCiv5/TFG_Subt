""" Objectiu: Obtenir les marques de temps de cada subfrase."""

import os 
import sys
import datetime 

#Variables marques de temps
marca_ini = 0.00
marca_fin = 0.00

#Obro fitxers de text de lectura
fT = open('002_frases.txt', 'r')
fL = open('arxiu73_words_002.lab', 'r')

for lin2 in fL:

  for lin1 in fL:

    while len(lin1):

      if(len(lin1) > 35):

        lin1_35 = lin1[0:35] 
 
        subf = lin1_35[:lin1_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat. 

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

        lin1 = lin1[lin1_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.

      else:

        subf = lin1[0:]

        par_begin = subf

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud. 
      
        lin1 = [] #Actualitzo valor resultant de línia.

  i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula.

  if(word == subf[0]):

    marca_ini = i_time

    print(marca_ini) 


fT.close()
fL.close()
