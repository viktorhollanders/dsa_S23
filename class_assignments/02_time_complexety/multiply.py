# The time complexety is O(n) where n is the number of times
# the function needs to add to gether x  y
def multiply(x, y):
    ret_value = 0
    for _ in range(y):
        ret_value += x

    return ret_value


print(multiply(2, 3))