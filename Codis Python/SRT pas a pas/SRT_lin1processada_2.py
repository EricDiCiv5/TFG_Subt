""" Objectiu: Ídem a 'SRT_lin1 processada.py' però fent-ho a travès d'una funció."""

import os 
import sys 


def proclinees (frase):

  #Funció que donada una frase la segmenta en subfrases de 35 caràcters máxim
  while len(frase):

    if(len(frase) > 35):

      frase_35 = frase[0:35] 
      subf = frase_35[:frase_35.rindex(' ')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

      print(subf," (longitud = ",len(subf),")") #Imprimeixo subfrase i la seva longitud

      frase = frase[frase_35.rindex(' ')+1:] #Actualitzo valor resultant de línia.
      
    elif (len(lin1) < 35):

      frase_x = frase[0:]
      subf = frase_x[:frase_x.index('\.')] #Variable 'subf' serà la subfrase fins al darrer espai trobat.

      print(subf," ( longitud = ",len(subf),")") #Imprimeixo subfrase i la seva longitud.

    return

#Obro fitxers de text de lectura
f1 = open('002_frases.txt', 'r') 

for lin1 in f1:

  proclinees(lin1) 

f1.close()
