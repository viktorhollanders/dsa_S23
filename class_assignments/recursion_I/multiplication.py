def multiply(val, count):
    if count == 0:
        return 0
    else:
        return val + multiply(val, count - 1)


print(multiply(2, 4))
