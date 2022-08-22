# Using Euclidean algorithm
def find_gcd(n1, n2):
    assert n1 == int(n1) and n2 == int(n2), 'Numbers have to be integers'

    if n1 < 0:
        n1 *= -1
    if n2 < 0:
        n2 *= -1

    if n2 == 0:
        return n1

    return find_gcd(n2, n1 % n2)


print(find_gcd(48, -18))

