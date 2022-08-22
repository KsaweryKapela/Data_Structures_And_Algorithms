def fibonacci(n):
    assert 0 <= n == int(n), 'Fibonnacci number cant be negative number or non int'
    print(n)
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)


def fizzbuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
    if n == 100:
        return None
    return fizzbuzz(n + 1)


fizzbuzz(1)

