import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def find_number(array, target):  # linear search
    for number in range(len(array)):
        if array[number] == target:
            return number


print(find_number(arr, 10))


def find_number(array, target):  # non linear
    og_array = array
    while True:
        splits = np.array_split(array, 2)
        for split_array in splits:
            if target in split_array:
                if len(split_array) == 1:
                    return np.where(og_array == int(split_array))
                array = split_array


print(find_number(arr, 10))
