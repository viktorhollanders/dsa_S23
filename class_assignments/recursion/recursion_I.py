def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)


def multiply(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return -a + multiply(a, b + 1)
    else:
        return a + multiply(a, b - 1)


def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)


def natural_numbers(n):
    if n > 0:
        return natural_numbers(n - 1) + " " + str(n)
    return " "


def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)


def fibonacci_pair(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci_pair(n - 1)
        return (a + b, a)


if __name__ == "__main__":
    print(fibonacci_pair(12))

    # print(sum_digits(254))
    # print(sum_digits(3578))

    # print(factorial(5))
    # print(multiply(2, 3))
    # print(multiply(-2, 3))

    # print(power(2, 3))
    # print(power(4, 5))
