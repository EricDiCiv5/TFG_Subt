""" Objectiu: llegir el fitxer .txt y 
printar per pantalla 2 línies de 35 caràcters
i una línia en blanc. 
"""

import os #Agafo les funcionalitats del sistema operatiu per connectar-lo amb l'entorn Python

import sys #Agafo funcions específiques del sistema

f = open('002_frases.txt', 'r') #Obro fitxer de lectura .txt assignant-ho a variable 'f'

for l in f:

	l35 = l[0:35]

	espai = l35[:l35.rindex(' ')]

	print(espai)

f.close()
