class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.array = [None] * self.capacity

    def __str__(self):
        ret_str = ""
        for i in range(0, self.size):
            ret_str += str(self.array[i]) + " "
        return ret_str

    def resize(self):
        if self.capacity == self.size:
            self.capacity *= 2
            temparr = [None] * self.capacity
            for i in range(0, self.size):
                temparr[i] = self.array[i]
            self.array = temparr

    def append(self, value):
        self.resize()
        self.array[self.size] = value
        self.size += 1

    def remove_largest(self):
        largest_num = 0
        index = 0

        for i in range(self.size):
            if self.array[i] > largest_num:
                largest_num = self.array[i]
                index = i
            continue

        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1


def count_in_range(lis, range_from, range_to):
    if len(lis) == 0:
        return 0
    elif range_from <= lis[0] <= range_to:
        return count_in_range(lis[1:], range_from, range_to) + 1
    else:
        return count_in_range(lis[1:], range_from, range_to)

    # if len lis == 0 return
    # if the number is in the range of range_from to range_to
    #  count the number
    # else pass


def count_oc():
    num = 1
    count = 0
    return count + num


def count_in_range_1(lis, range_from, range_to):
    if range_to > len(lis):
        return count_in_range_1(lis, range_from, range_to=len(lis) - 1)

    if lis[range_from] == lis[range_to]:
        return count_oc()
    else:
        return count_in_range_1(lis, range_from + 1, range_to) + count_oc()


def remove_odd_indexes(lis):
    # if the index is odd remove the item at that index from the list

    # else keep the item
    return lis


if __name__ == "__main__":
    print("Arraylist tests:")
    arrlis = ArrayList()
    arrlis.append(8)
    arrlis.append(62)
    arrlis.append(15)
    arrlis.append(19)
    arrlis.append(24)
    arrlis.append(7)
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    arrlis.remove_largest()
    print(arrlis)
    print("Recursion tests:")
    print(count_in_range([5, 1, 22, 7, 19, 8, 31, 4, 6, 10, 17, 13], 5, 20))
    print(count_in_range([5, 1, 22, 7, 19, 8, 31, 4, 6, 10, 17, 13], 1, 5))
    print(count_in_range([5, 1, 22, 7, 19, 8, 31, 4, 6, 10, 17, 13], 0, 25))
    print(count_in_range([5, 1, 22, 7, 19, 8, 31, 4, 6, 10, 17, 13], 0, 100))
    print(remove_odd_indexes([5, 1, 22, 7, 19, 8, 31, 4, 6, 10, 17, 13]))
