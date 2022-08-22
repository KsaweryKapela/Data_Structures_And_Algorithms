def power(base, expoment):
    assert 0 <= expoment == int(expoment), 'Exponent cant be negative  or non int'
    if expoment == 0:
        return 1
    if expoment == 1:
        return base
    return base * power(base, expoment - 1)


print(power(3.2, 4))

