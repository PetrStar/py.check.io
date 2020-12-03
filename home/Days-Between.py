def days_diff(a, b):
    import datetime
    a, b = datetime.date(*a), datetime.date(*b)
    return abs(int(str(b - a).split()[0])) if a != b else 0


if __name__ == '__main__':
    print("Example:")
    print(days_diff((2014, 1, 27), (2014, 1, 1)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")