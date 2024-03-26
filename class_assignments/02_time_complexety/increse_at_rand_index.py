from random import randint

size = 10
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# The time complexety is O(1) beacuse we dont need to loop through the list
def incres_rand_num(a_list):
    random_index = randint(1, size)
    a_list[random_index] += 1
    return a_list


print(f"The original list: {a_list}")
a_list = incres_rand_num(a_list)
print(f"The updated list: {a_list}")
