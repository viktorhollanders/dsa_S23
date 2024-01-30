import random


def print_rand_num_list(size):
    a_list = ["0"] * size

    for index, _ in enumerate(a_list):
        random_num = random.randint(1, 6)
        a_list[index] = str(random_num)

        # print to the screen
        print(random_num)
        print(", ".join(a_list))


print_rand_num_list(5)
