def last_digit(n1, n2):
    result = n1
    if n2 == 0:
        return 1
    for n in range(n2 - 1):
        result *= n1
    return int(str(result)[-1])

## very slow arlgorithm TODO: do it better!