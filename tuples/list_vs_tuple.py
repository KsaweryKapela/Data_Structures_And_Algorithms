list_1 = [1, 2, 3]
list_1 = [3, 2, 1]

print(list_1)

tuple_1 = (1, 2, 3)
tuple_1 = (3, 2, 1)

print(tuple_1)  # Both are possible

# tuple_1[0] = 3 -> impossible
# del tuple_1[0] -> impossible

# reverse, append, insert, remove etc. -> impossible on tuples

list_of_tuples = [(1, 2, 3), (1, 2, 3)]

print(list_of_tuples)

tuple_of_lists = ([1, 2, 3], [1, 2, 3])

print(tuple_of_lists)

tuple_of_tuples = ((1, 2, 3), (1, 2, 3))

print(tuple_of_tuples)

# Tuples for heterogeneous (different) data types, lists for homogeneous
# Iterating is faster through tuple
# Tuples with immutable elements can be used as keys in dict
# If data should not be changed, its good idea to put it in tuple
