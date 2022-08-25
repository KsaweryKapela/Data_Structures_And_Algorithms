from random import randint

# populating list
random_list = []
non_unique_list = []

for number in range(30):
    random_list.append(randint(1, 100))

print(random_list)
#  solution
for n in random_list:
    if n in random_list[:random_list.index(n)] + random_list[random_list.index(n) + 1:]:
        if n not in non_unique_list:
            non_unique_list.append(n)
            print('list is not unique, because of', n)


