# immutable, comparable, hashable (can be used as keys)
# immutable means unchangeable unlike lists

new_tuple = 'a', 'b', 'c', 'd'  # -> parenthesis are only convention. O(1), SC O(n)
tuple_2 = ('a')  # -> it's just a string
tuple_3 = ('a',)  # -> tuple, because of coma

empty_tuple = ()
empty_tuple_2 = tuple('xxx')

print(new_tuple)
print(type(tuple_2))
print(type(tuple_3))

print(empty_tuple)
print(empty_tuple_2)  # Threats every single letter of string as different string element

print(new_tuple[0])
print(new_tuple[1:3])  # Same as lists, but can't modify elements

for i in new_tuple:
    print(i)

for i in range(len(new_tuple)):  # O(n), traversing through tuple
    print(new_tuple[i])

print('b' in new_tuple)  # True/False


def search_tuple(your_tuple, element):
    for item in your_tuple:
        if item == element:
            return your_tuple.index(item)
    return 'The element does not exist'


print(search_tuple(new_tuple, 'b'))  # Search in tuple O(n)

print(new_tuple + tuple_3)

print(new_tuple * 3)

print(new_tuple.count('a'))

print(new_tuple.index('c'))

print(len(new_tuple))

print(min(new_tuple))

list_to_tuple = tuple(['list_element', 'list_element'])

print(list_to_tuple)