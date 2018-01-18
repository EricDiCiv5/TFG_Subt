""" Objectiu: Processar cada línia del fitxer "002_frases.txt" a un máxim de 35 caràcters 
i printar per pantalla la sublínia més el número de la seva longitud."""

import os 
import sys 

num_subt = 1 #Contador del número de subtítol

#Obro fitxers de text de lectura
f1 = open('002_frases.txt', 'r') 

for lin1 in f1:

  while len(lin1):

    lin1_35 = lin1[0:35] 

    subf = lin1_35[:lin1_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

    print(subf," (longitud = ",len(subf),")") #Imprimeixo subfrase i la seva longitud

    lin1 = lin1[lin1_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.

    if (len(lin1) < 35):

      lin1_x = lin1[0:end]

      subf = lin1_x[:lin1_x.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

      print(subf," (longitud = ",len(subf),")") #Imprimeixo subfrase i la seva longitud.

f1.close()
