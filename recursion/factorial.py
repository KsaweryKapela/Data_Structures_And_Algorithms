def factorial(n):
    assert 0 <= n == int(n), 'Factorial cant be negative or non int'
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(7))
