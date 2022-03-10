import random

wordscas = """abran
abras
abras
abria
acoja
acojo
acres
actuo
acuna
acuna
acuna
acuna
aguda
agudo
alaju
albos
alias
alojo
aloja
alojo
altas
alias
amina
amina
ancas
andas
andes
andes
anima
anima
aojar
aojas
aojos
aojas
apoda
apodo
apoda
apodo
apure
arces
arcos
ardan
ardas
ardes
ardas
ardes
arias
arios
arlos
arpas
aruba
areis
asees
aseos
asire
asolo
aseis
asian
asias
atoja
atojo
atoja
atojo
avale
avara
azote
aerea
echas
eches
echos
eches
edita
edita
eleve
ellos
emoji
emoyi
emues
enoja
enojo
enoja
entes
envio
erizo
errar
erres
erres
espia
estad
estas
euros
evita
evita
ibais
iglus
india
intis
ireis
irian
irias
isbas
islas
obras
ollas
omani
ombus
ondas
onzas
opera
opera
orcas
orden
ornan
oseas
oseas
otras
ovulo
untes
urdas
urnas
usaos
usate
useis
uñoso
"""

wordslist = wordscas.split('\n')
outputwordslist = []

for i in range(len(wordslist)-1):

    selected = wordslist[i]

    if "".join(dict.fromkeys(selected)) == selected and len(selected) == 5:
    #checks if there are any repeating letters and if the length of the word is 5

        outputwordslist.append(selected)

def get_casword():
    return random.choice(outputwordslist).lower()
