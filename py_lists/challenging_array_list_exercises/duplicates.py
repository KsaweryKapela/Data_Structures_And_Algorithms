arr = [1, 1, 2, 2, 3, 4, 5]


def remove_duplicates(lst):
    new_list = []
    for n in lst:
        if n not in new_list:
            new_list.append(n)

    return new_list


print(remove_duplicates(arr))
