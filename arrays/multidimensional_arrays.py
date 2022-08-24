import numpy as np

dd_arr = np.array([[11, 15, 10, 6],
                   [10, 14, 11, 5],
                   [12, 17, 12, 8],
                   [15, 18, 14, 9]]) # O(1)

dd_arr_1 = np.insert(dd_arr, 0, [[1, 2, 3, 4]], axis=1)  # axis = 0/1 : row/column O(nm)/O(1)

dd_arr_2 = np.append(dd_arr_1, [[1, 2, 3, 4, 5]], axis=0)  # O(1)


def access_2d_elements(arr, row_index, column_index):
    if row_index >= len(arr) or column_index >= len(arr[0]):
        return 'Index error'

    return arr[row_index][column_index]


print(dd_arr_2)
print(access_2d_elements(dd_arr_2, 4, -5))  # O(1)


def traverse_2d_array(arr):
    for row in arr:
        for i in row:
            print(i)


def alt_traverse_2d_array(arr):
    for row in range(len(arr)):
        for column in range(len(arr[0])):
            print(arr[row][column])


alt_traverse_2d_array(dd_arr_2)  # O(mn) or O(n^2) if len(row) == len(column)


def linear_search_2d_arr(arr, value):
    for row in range(len(arr)):
        for column in range(len(arr[0])):
            if arr[row][column] == value:
                return f"Value is at index {row}, and {column}"
    return 'Element is not on the list'


print(linear_search_2d_arr(dd_arr_2, 51))  # O(nm) or...

dd_arr_3 = np.delete(dd_arr_2, 0, axis=1) # O(nm)/O(1) if it's last row/column or...

print(dd_arr_2)
print(dd_arr_3)
