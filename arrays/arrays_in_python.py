from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])

arr1.insert(2, 7)  # O(n) - because part of array need to move right
arr1.insert(7, 7)  # O(1)


def traverse_array(array_):
    for i in array_:
        print(i)


traverse_array(arr1)  # O(n)


def access_element(array_, index):
    if index > len(array_) - 1 or index < len(array_) * -1:
        print('Index error')
    else:
        print(array_[index])


access_element(arr1, -8)  # O(1)


def search_in_array(array_, value):
    for i in array_:
        if i == value:
            return array_.index(value)
    return 'The element does not exist in the array'


print(search_in_array(arr1, 7))  # O(n)

arr1.remove(2)  # O(n) - because rest of array has to move. Deleting last element = O(1)


