my_dict = {1: 1, '1': 2, 1.0: 4}

dict_sum = 0

for k in my_dict:
    dict_sum += my_dict[k]

print(dict_sum)  # 1 == 1.0 -> True

#

a = {(1, 2): 1, (2, 3): 2}
print(a[1, 2])  # [1, 2] checks index (1, 2)

#

rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id1 = id(rec)
del rec
rec = {"Name": "Python", "Age": "20", "Addr": "NJ", "Country": "USA"}
id2 = id(rec)
print(id1 == id2)  # since dicts are the same, the ids are the same

#

quiz_dict = {'c': 97, 'a': 96, 'b': 98}

for _ in sorted(quiz_dict):
    print(quiz_dict[_])  # It's sorted by keys, so a, b, c
