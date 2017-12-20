""" Objectiu: printar per pantalla el format dle fitxers .SRT 
havent llegit la marca inicial, la marca final i la paraula 
"""

import os #Agafo les funcionalitats del sistema operatiu per connectar-lo amb l'entorn Python

import sys #Agafo funcions específiques del sistema

f2 = open('arxiu73_words_002.lab', 'r') #Obro fitxer .lab assignant-ho a variable 'f2'

num_subt = 1 #defineixo un enter que actuarà com a contador del número de subtítol a processar i mostrar

for labline in f2:

 i_time,f_time,word = labline.split(' ') #Parteixo la línia en 3 paràmetres: marca inicial de temps, marca final i la paraula

 print(num_subt) #Mostro per pantalla el número de subtítol a processar

 print(i_time,"-->",f_time) #Mostro per pantalla les marques inicial i final separades pels caràcters ' --> '

 print(word) #Mostro la paraula subtitulada

 num_subt += 1 #Incremento en una unitat el número del subtítol    

f2.close() #Tanco el fitxer contingut en la variable 'f2'
