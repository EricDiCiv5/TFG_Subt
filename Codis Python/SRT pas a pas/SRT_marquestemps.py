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


for lin1 in fT:

  while len(lin1):

    if(len(lin1) > 35):

      lin1_35 = lin1[0:35] 
 
      subf = lin1_35[:lin1_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

      for lin2 in fL.readlines():

        i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula.

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

        if(word == subf[0]):
        
          marca_ini = i_time

          ini_t = str(datetime.timedelta(marca_ini))

        if(word == subf[-1]):

          marca_fin = f_time

          fin_t = str(datetime.timedelta(marca_fin))

        print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

      lin1 = lin1[lin1_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.

    else:

      subf = lin1[0:]
  
      print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.
  
      lin1 = [] #Actualitzo valor resultant de línia.

fT.close()
fL.close()

