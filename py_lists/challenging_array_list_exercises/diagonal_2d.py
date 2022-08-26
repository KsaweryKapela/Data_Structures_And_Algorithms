myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sum_diagonal(arr_2d):
    diagonal_sum = 0

    for i in range(len(arr_2d)):
        diagonal_sum += arr_2d[i][i]

    return diagonal_sum


print(sum_diagonal(myList2D))