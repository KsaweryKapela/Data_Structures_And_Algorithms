myList = [120, 100, 84, 85, 86, 87, 85, 90, 85, 83, 23, 122, 45, 84, 1, 2, 0, 130]


def first_second(arr):  # My fix
    first_score = arr[0]
    second_score = arr[-1]

    for number in arr[1:]:
        if number >= first_score:
            second_score = first_score
            first_score = number

        elif number > second_score:
            second_score = number

    return first_score, second_score


print(first_second(myList))


def first_second_course(given_list):  # course fix - using sort
    a = given_list  # make a copy

    a.sort(reverse=True)

    first = a[0]

    second = None

    for element in given_list:

        if element != first:
            second = element

            return first, second
