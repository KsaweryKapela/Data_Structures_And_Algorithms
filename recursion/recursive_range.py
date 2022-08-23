def recursive_range(num):
    if num == 1:
        return num
    return num + recursive_range(num - 1)


print(recursive_range(10))

