# A ineficient way of doing the fibonacci

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


# A efficient way of doing fibonacci

    