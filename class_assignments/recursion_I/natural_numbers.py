def natural_number(n):
    if n == 0:
        return 0
    natural_number(n - 1)
    print(n, end=" ")


natural_number(5)
