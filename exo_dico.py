# 1. Créer un dictionnaire appelé notes avec au moins 3 personnes

notes = {
    "Alice": 12,
    "Bob": 13,
    "Charlie": 10,
}

# 2. Remplacer la note d'un élève existant par 15

notes["Alice"] = 15

# 3. Ajouter un nouvel élève et sa note

notes["Donald"] = 17

# 4. Afficher la note du second élève

print(notes["Bob"])
print(list(notes.values())[1])

# 5. Afficher la moyenne des notes

mean_val = 0

for key, value in notes.items():
    mean_val += value

print(mean_val / len(notes))

mean_val = 0
for value in notes.values():
    mean_val += value

print(mean_val / len(notes))

