def example_function(a: int, b: int, c: int) -> float:
    return (a * b) / c - (a * c) / b

example = example_function
print(type(example))
print(example(2, 5, 9.6))

my_str = "Hello, World!"

print(my_str.split(","))


def calcul_moyenne(tab: list) -> float:
    total = 0
    for num in tab:
        total += num
    
    return total / len(tab)


def calcul_moyenne_2(*args) -> float:
    total = 0
    for num in args:
        total += num
    
    return total / len(args)


print(calcul_moyenne_2(2, 9, 5, 3, 6, 9, 8, 5, 2, 36, 9, 8, 22, 6, 63, 5))

def recherche_min(tab: list) -> int:
    min_value = tab[0]
    for num in tab:
        if num < min_value:
            min_value = num
    
    return min_value

print(recherche_min([2, 9, 5, 3, 6, 9, 8, 5, 2, 36, 9, 8, 22, 6, 63, 5]))


def generer_email(nom: str, prenom: str):
    return f"{prenom.lower()}.{nom.lower()}@example.com"

print(generer_email("Doe", "John"))


def compter_mots(phrase: str) -> int:
    phrase = phrase.replace(",", "").replace("?", "").replace("!", "").replace("-", " ").replace("'", " ")
    mots = phrase.split(" ")
    return len(mots)

print(compter_mots("Bonjour, comment ça va ?"))


def convertir_celsius_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

print(convertir_celsius_fahrenheit(25), "°F")
