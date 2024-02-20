def multiply(a, b):
    # for every iteration multiply the current base with the base
    ret_val = 0
    for _ in range(b):
        ret_val += a
    return ret_val


print(multiply(4, 5))
print(multiply(3, 4))
#O(n)