arr = [1, 2, 3, 4, 5, 6, 7]


def missing_number(lst, proper_len):
    counter = 1

    for n in range(proper_len):
        try:
            if lst[n] != counter:
                return counter
            counter += 1

        except IndexError:
            return lst[-1] + 1


print(missing_number(arr, 8))


def missing_number_course(lst, proper_len):
    expected_sum = (proper_len * (proper_len + 1)) / 2
    actual_sum = 0

    for i in lst:
        actual_sum += i

    return int(expected_sum - actual_sum)


print(missing_number_course(arr, 8))
