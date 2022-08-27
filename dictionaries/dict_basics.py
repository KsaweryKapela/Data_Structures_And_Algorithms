my_dict = dict()
my_dict2 = {}
print(my_dict)

eng_spn = {"one": "uno",
           "two": "dos",
           "three": "tres"}

print(eng_spn['one'])  # O(1)

eng_spn['one'] = 'unos!'  # O(1)

eng_spn['four'] = 'quatro'  # O(1), space complexity = amortized O(1) -> it becomes O(n) if data structure grows


def traverse_dict(dictionary):
    for key in dictionary:
        print(key, dictionary[key])


traverse_dict(eng_spn)  # O(n)


def search_dict(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key, value
    return 'The value doesnt exist'


print(search_dict(eng_spn, 'tres'))  # O(n)

print(eng_spn.pop('three'))

print(eng_spn)

eng_spn.popitem()

print(eng_spn)

del eng_spn['one']

print(eng_spn)

eng_spn.clear()

print(eng_spn)

del eng_spn

# O(1), in worst, amortised case O(n)