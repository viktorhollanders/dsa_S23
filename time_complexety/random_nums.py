import random


def rand_num_list(size):
    a_list = [0] * size

    for index, _ in enumerate(a_list):
        a_list[index] = random.randint(1, 6)
    return a_list


print(rand_num_list(5))
# O(1)



