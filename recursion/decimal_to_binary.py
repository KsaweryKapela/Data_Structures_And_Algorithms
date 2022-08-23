def decimal_to_binary(n):
    assert 0 <= n == int(n), 'Decimal cant be negative or non int'
    if n == 0 or n == 1:
        return n
    return n % 2 + 10 * decimal_to_binary(n // 2)


print(decimal_to_binary(13))
