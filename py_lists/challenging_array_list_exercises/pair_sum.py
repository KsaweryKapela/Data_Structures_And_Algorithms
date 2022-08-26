arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]


def pair_sum(lst, number):
    pair_list = []
    for n in range(len(lst)):
        for i in range(n, len(lst)):
            if lst[n] + lst[i] == number:
                pair_list.append(f'{lst[n]} + {lst[i]}')
    return pair_list


print(pair_sum(arr, 7))
