""" Objectiu: Obtenir les marques de temps de cada subfrase."""

import os 
import sys
import datetime 

#Variables marques de temps
marca_ini = 0.00
marca_fin = 0.00

with open('002_frases.txt', 'r') as fT, open('arxiu73_words_002.lab') as fL:

  for lin1, lin2 in zip(fT, fL):

    while len(lin1):

      if(len(lin1) > 35):

        lin1_35 = lin1[0:35] 

        subf = lin1_35[:lin1_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

        par_begin = subf[0:subf.rindex(' ')] #Agafo la primera paraula de la subfrase. 

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

        lin1 = lin1[lin1_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.

      else:

        subf = lin1[0:]

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.. 
      
        lin1 = [] #Actualitzo valor resultant de línia.

        i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula

        if(word == subf):

          marca_ini = i_time

          print(marca_ini) 

fT.close()
fL.close()
