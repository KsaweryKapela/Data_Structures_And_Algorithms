def sum_of_digits(n):
    assert 0 <= n == int(n), 'Number cant be negative  or non int'
    if len(str(n)) == 1:
        return n
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(2130000000123))

