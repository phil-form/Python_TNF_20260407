# exo16-Un algorithme reçoit deux nombres de l’utilisateur (input) : a et b.

# Il répond : « C’est plus » lorsque b est plus petit que a.

# Et inversement, il répond : « C’est moins » lorsque b est plus grand que a.

# Si a est égal à b, il répond : « C’est gagné ».

# Vous aurez besoin de la librairie random pour générer un nombre aléatoire.

import random

# Générer un nombre aléatoire entre 1 et 100
a = random.randint(1, 100)

nombre_entre = int(input("Devinez le nombre entre 1 et 100 : "))

while nombre_entre != a:
    if nombre_entre < a:
        print("C'est plus !")
    else:
        print("C'est moins !")
    nombre_entre = int(input("Essayez à nouveau : "))
    


while True:
    nombre_entre = int(input("Devinez le nombre entre 1 et 100 : "))
    
    if nombre_entre < a:
        print("C'est plus !")
    elif nombre_entre > a:
        print("C'est moins !")
    else:
        print("C'est gagné !")
        break

found = False

while not found:
    nombre_entre = int(input("Devinez le nombre entre 1 et 100 : "))

    if nombre_entre < a:
        print("C'est plus !")
    elif nombre_entre > a:
        print("C'est moins !")
    else:
        print("C'est gagné !")
        found = True

