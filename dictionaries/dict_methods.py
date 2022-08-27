random_dict = {
    'name': 'Ksaw',
    'surname': 'Kap',
    'brother': 'Kac',
    'girl': 'An'
}

copy_of_dict = random_dict.copy()

new_dict = {}.fromkeys([1, 2, 3], 0)
print(new_dict)

print(random_dict.get('surname', ''))  # Kap
print(random_dict.get('', 'Kap'))  # Kap

print(random_dict.items())

print(random_dict.keys())

print(random_dict.values())

print(random_dict.popitem())

random_dict.setdefault('name_full', 'Ksawery')

print(random_dict)

new_dict = {'a': 'b',
            'c': 'd'}

random_dict.update(new_dict)

print(random_dict)

if 'a' in random_dict:  # Only keys, .values for values. time complexity O(1), because of hash.
    print('a is in dict')

bool_dict = {1: True, 2: 'True', 3: True}
print(all(bool_dict))

false_dict = {1: False, 2: False, 3: False}
print(all(false_dict))  # Weirdly returns True, even tho course said it should be False

print(any(false_dict))
print(any(bool_dict))  # Weirdly returns True, even tho course said it should be False

print(len(bool_dict))  # No of pairs

print(sorted(random_dict, reverse=True, key=len))
