def flatten(arr):
    if len(arr) == 0:
        print(arr)
        return arr
    if type(arr[0]) == int:
        print('int')
        if not arr[1:]:
            return [[arr[0]]]

        return sum([[arr[0]], flatten(arr[1:])], [])

    else:
        print('list')
        return sum([[flatten(arr[0])], flatten(arr[1:])], [])


print(flatten([1, [2, [3, 4], [[5]]]]))


# Still looking for a fix, just not gona finish it now.
