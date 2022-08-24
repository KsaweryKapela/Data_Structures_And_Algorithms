from array import *

arr = array('i', [1, 2, 3, 4, 5])

# traverse

for i in arr:
    print(i)

# access element

print(arr[0])

# append

arr.append(2)

# insert

arr.insert(5, 2)

# extend

arr1 = array('i', [10, 11, 12])

arr.extend(arr1)

# fromList

temp_list = [1, 2, 3, 23]
arr.fromlist(temp_list)

# remove

arr.remove(23)

# pop

arr.pop()

# index

print(arr.index(2))

# reverse

arr.reverse()

# buffer_info

print(arr.buffer_info())

# count

print(arr.count(2))

# to list

list_temp = arr.tolist()
print(list_temp)

# slice

print(arr[:3])