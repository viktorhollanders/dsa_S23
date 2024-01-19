def power(base, exp):
    # for every iteration multiply the current base with the base
    ret_val = 1
    for _ in range(exp):
        ret_val *= base
    return ret_val


print(power(2, 8))
print(power(2, 10))

#O(n)

