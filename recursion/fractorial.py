def fractorial(n):
    if n == 1:
        return 1
    return fractorial(n - 1) * n


print(fractorial(5))
