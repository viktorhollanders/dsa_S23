# time cokplexety O(n)
def power(base, expo):
    ret_value = 1
    for _ in range(expo):
        ret_value *= base
    return ret_value


print(power(2, 8))
print(power(2, 2))
