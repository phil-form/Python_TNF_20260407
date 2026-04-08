annee = int(input("Entrer un nombre : "))

if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print(f"{annee} est bisextile.")
else:
    print(f"{annee} n'est pas bisextile.")