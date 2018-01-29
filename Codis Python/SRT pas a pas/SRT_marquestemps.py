""" Objectiu: Obtenir les marques de temps de cada subfrase."""

import os 
import sys 

#Obro fitxers de lectura
fT = open('002_frases.txt', 'r')
fL = open('arxiu73_words_002.lab','r')

#Variables marques de temps
marca_ini = 0.00
marca_fin = 0.00

for lin1 in fT:

  while len(lin1):

    if(len(lin1) > 35):

      lin1_35 = lin1[0:35] 

      subf = lin1_35[:lin1_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

      print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

      lin1 = lin1[lin1_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.

      par_begin = subf[0:subf.index(' ')] #Agafo la primera paraula de la subfrase.

      par_end = subf[subf.rindex(' ')+1:] #Agafo la darrera paraula de la subfrase.



      while fL.readline():

        lin2 = fL.readline()

        i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula

        if(par_begin == word):

          marca_ini = i_time 

        if(par_end == word):

          marca_fin = f_time 



    else:

      subf = lin1[0:]

      print(len(subf),"/",len(lin1),":",subf) #Imprimeixo subfrase i la seva longitud.

      lin1 = [] #Actualitzo valor resultant de línia.



      if(subf.find(' ')):

        par_begin = subf[0:subf.index(' ')] #Agafo la primera paraula de la subfrase.

        par_end = subf[subf.rindex(' ')+1:] #Agafo la darrera paraula de la subfrase.

      while fL.readline():

        lin2 = fL.readline()

        i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula

        if(par_begin == word):

          marca_ini = i_time 

        if(par_end == word):

          marca_fin = f_time



      else:

        par = subf[0:]


         
        while fL.readline():

          lin2 = fL.readline()

          i_time,f_time,word = lin2.split() #Parteixo línia en tres paràmetres: marca inicial, marca final i la paraula

          if(par_begin == word):

            marca_ini = i_time 

          if(par_end == word):

            marca_fin = f_time 



fT.close()
fL.close()
