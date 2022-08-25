my_list = [2, 4, 1, 2]

x = my_list.sort()
print(x)  # None

my_list = [2, 4, 1, 2]

original_list = my_list[:]
my_list.sort()
print(original_list)  # OG list
print(my_list)  # Sorted list

my_list = [2, 4, 1, 2]
sorted_list = sorted(my_list)
print(my_list)  # OG list
print(sorted_list)  # Sorted list
