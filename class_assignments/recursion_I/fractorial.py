def fractorial(n):
    if n == 0:
        return 1
    else:
        return n * fractorial(n - 1)


print(fractorial(5))
