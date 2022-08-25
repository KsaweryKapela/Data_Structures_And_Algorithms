# mutable data structures - we can change order or reassign item

ints = [1, 2, 3, 4]

strings = ['xxx', 'yy', 'z']

mix = [1, 'z', 2.1, ['x', {'x': 'y'}]]

int0 = ints[0]  # Mapping - each index maps list element.

print(1 in ints)  # returns boolean

for i in ints:  # O(n), traversing
    print(i)

for i in range(len(ints)):  # O(n), traversing
    print(ints[i])

ints[0] = 33  # O(1)

print(ints)

ints.insert(3, 41)  # O(1) or O(n)

ints.append(55)  # O(1)

ints2 = [24, 123, 99]

ints.extend(ints2)  # O(n)

print(ints[:])

ints.pop(5)  # if last element O(1) else O(n)

del ints[0]  # if last element O(1) else O(n)

ints.remove(123)  # if last element O(1) else O(n)

print(ints)

if 99 in ints:  # O(n)
    print('yay', + ints.index(99))
else:
    print('nay')


def search_in_list(py_list, value):
    for i in py_list:
        if i == value:
            return py_list.index(value)
    else:
        return "Can't find it"


print(search_in_list(ints, 100))  # O(n) linear search

ints = ints + ints2

ints = ints * 3

len(ints)  # O(n)

print(sum(ints))
