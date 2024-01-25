def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        print(fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(10)
