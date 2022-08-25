#  Here fruit_list_1 also changes, just on the basis that it equals fruit_list2

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1

fruit_list2[0] = 'Guava'

print(fruit_list1)


# Here values keep growing, despite first being defined empty list variable.
def f(i, values=[]):
    values.append(i)
    print(values)
    return values


f(1)
f(2)
f(3)


def x(new_letter, letters=[]):
    letters.append(new_letter)
    print(letters)


x('b')
x('c')  # it returns ['b', 'c'], so list(letters) defined in variable gets changed and stays changed.

#  It sliced [3] to [0] and :-1 means the slicing direction is reserved (it goes from right to left).
a = [1, 2, 3, 4, 5]
print('x', a[3:0:-1])


# It loops through first 2d list, so [[1, 2], [3, 4]] and finds the biggest number.
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v


data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(fun(data[0]))
