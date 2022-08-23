def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def some_recursive(arr, cb):
    if not len(arr):
        return False
    if is_odd(arr[0]):
        return True
    else:
        return some_recursive(arr[1:], cb)
