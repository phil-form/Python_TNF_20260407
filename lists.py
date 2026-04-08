from functools import cmp_to_key

data = [1,2,3,4,5,6,7,8,9,10]

def sort_mod_2(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return 0
    elif a % 2 == 0 and b % 2 == 1:
        return 1
    else:
        return -1

data = sorted(data, key=cmp_to_key(sort_mod_2))

print(data)

a, b = 1, 3

def tuple_example():
    return 1, 2, 3

a, b, c = tuple_example()

my_list = list((a, b, c))
my_tuple = tuple((a, b, c))

elem = my_list[0]

# [22, 2, 3]
my_list[0] = 22

set_example = set(my_list)
print(set_example)
set_example.add(22)
print(set_example)

if 22 in set_example:
    print("has 22")

my_list3 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(my_list3)
print(set(my_list3))

dictionary = {
    "nom": "Test",
    "prenom": "Philippe",
}

print(dictionary["nom"])
dictionary["prenom"] = "Tralala"

number_of_occurence = {}

for val in my_list3:
    number_of_occurence[val] = number_of_occurence.get(val, 0) + 1

print(number_of_occurence)