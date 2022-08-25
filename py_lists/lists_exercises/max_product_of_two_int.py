import numpy as np

arr = np.array([13, 30, 3, 2, 1, 23, 7, 10, 9, 10])


def find_max_outcome(array):
    max_n = 0
    pairs = None
    for n in range(len(array)):
        for i in range(n + 1, len(array)):
            if array[n] * array[i] > max_n:
                max_n = array[n] * array[i]
                pairs = str(array[n]) + ', ' + str(array[i])
    return max_n, pairs


print(find_max_outcome(arr))