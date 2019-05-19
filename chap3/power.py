def power(base, exponent):
    """求指数"""
    try:
        result = power_with_unsigned_exponent(base, abs(exponent))
        if exponent < 0:
            return 1/result
        else:
            return result
    except ZeroDivisionError:
        print("Error: base is zero and exponet is negative.")
        return None


def power_with_unsigned_exponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    result = power_with_unsigned_exponent(base, exponent >> 1)
    result *= result
    if exponent & 1 == 1:
        result *= base

    return result


if __name__ == '__main__':
    array = [-2, 2, 0]
    for base in array:
        for exponent in array:
            print(power(base, exponent))
