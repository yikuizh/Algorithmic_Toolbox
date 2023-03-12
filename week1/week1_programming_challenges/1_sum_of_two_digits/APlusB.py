def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    """ understand if __name__ == '__main__'
    if run .py directly this part will run directly
    but .py introduced as a file, code below will not be excuted
    """
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
