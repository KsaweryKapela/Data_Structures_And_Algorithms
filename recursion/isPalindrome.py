def is_palindrome(string):

    if len(string) in [0, 1]:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


print(is_palindrome('xxx'))