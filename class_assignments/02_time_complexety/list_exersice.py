import random

# the time complexety of this operaton is O(n)


def insert_rand_num(size):
    a_list = [0] * size
    for item in range(size):
        a_list[item] = random.randint(1, 6)

    return a_list


num_list = insert_rand_num(5)
print(num_list)


def print_to_screen(num_list):
    ret_value = ""
    size = len(num_list)
    for index, item in enumerate(num_list):
        if index == size - 1:
            ret_value += f"{item}"
        else:
            ret_value += f"{item}, "

    print(ret_value.strip())


print_to_screen(num_list)


# Version 2 of print to screen
def print_rand_num_list(size):
    a_list = ["0"] * size

    for index, _ in enumerate(a_list):
        random_num = random.randint(1, 6)
        a_list[index] = str(random_num)

        # print to the screen
        print(random_num)
        print(", ".join(a_list))


print_rand_num_list(5)
