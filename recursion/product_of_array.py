def product_of_array(array):
    if len(array) == 1:
        return array[0]
    return array[0] * product_of_array(array[1:])


print(product_of_array([10.5, 123.123, -2]))
