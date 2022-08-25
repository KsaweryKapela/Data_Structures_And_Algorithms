arr_1 = [1, 2, 3, 4, 1]
arr_2 = [3, 4, 2, 1, 1, 3]


def permutation(list1, list2):  # with deleting items from list
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] in list2:
            list2.remove(list1[i])
        else:
            return False
    return True


def permutation2(list1, list2):  # with sort
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


print(permutation2(arr_1, arr_2))
