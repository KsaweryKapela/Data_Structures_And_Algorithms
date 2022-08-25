from random import randint

# Creating random list with missing number

random_number = randint(1, 100)

list_missing_number = []
for number in range(1, 101):
    if number != random_number:
        list_missing_number.append(number)

# Solution of problem


def find_missing(list_, proper_no_elements):
    proper_list_sum = proper_no_elements * (proper_no_elements + 1) / 2
    answer = proper_list_sum - sum(list_)
    return answer


if find_missing(list_missing_number, 100) == random_number:
    print('The answer is', random_number)
