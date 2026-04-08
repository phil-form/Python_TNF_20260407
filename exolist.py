my_list = []

for i in range(1, 11):
    my_list.append(2 ** i)

print(my_list)

my_list = [2 ** i for i in range(1, 11)]
print(my_list)

for val in my_list:
    print(val)