import numpy as np
ddd_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def twist_matrix_right(arr):  # my solution
    list_of_arrays = []
    for i in range(len(arr)):

        arr_x = np.flip(np.array(arr[..., i]))
        list_of_arrays.append(arr_x)
    twisted_array = np.row_stack(list_of_arrays)
    return twisted_array


print(twist_matrix_right(ddd_array))


def rotate_matrix(arr):  # course solution, needs more review
    n = len(arr)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            top = arr[layer][i]
            arr[layer][i] = arr[-i-1][layer]
            arr[-i - 1][layer] = arr[-layer-1][-i-1]
            arr[-layer - 1][-i - 1] = arr[i][-layer-1]
            arr[i][-layer - 1] = top

    return arr


print(rotate_matrix(ddd_array))

