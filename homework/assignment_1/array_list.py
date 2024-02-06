class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.ordered = True # checks if the list is orderd

    # Time complexity: O(n) - linear time in size of list
    def __str__(self):
        """The str function prints the content of the string if it is not the last item add a space and comma in bewtween"""
        return_string = ""

        for i in range(0, self.size):
            if i == self.size - 1:
                return_string += str(self.arr[i])
            else:
                return_string += f"{self.arr[i]}, "

        return return_string

    # Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.resize()
        self.insert(value, 0)

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # The if check for the resize is in the resize function
        self.resize()
        self.check_index_out_of_bounds(index, self.size)
        # start at the end of the list
        for i in range(self.size, index - 1, -1):
            if i != 0 and i != index:
                self.arr[i] = self.arr[i - 1]

            if i == index:
                self.arr[i] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if index == 0:
            self.check_index_out_of_bounds(index, self.size - 1)

        self.check_index_out_of_bounds(index, self.size - 1)

        for i in range(0, self.size):
            if i == index:
                self.arr[index] = value

    # Time complexity: O(1) - constant time
    def get_first(self) -> list:
        self.check_empty(self.size)
        return self.arr[0]

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.size < 0:
            self.check_index_out_of_bounds(index, self.size - 1)

        self.check_index_out_of_bounds(index, self.size - 1)
        for i in range(0, self.size):
            if i == index:
                return self.arr[i]

    # Time complexity: O(1) - constant time
    def get_last(self):
        self.check_empty(self.size)
        return self.arr[self.size - 1]

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        ''' Checks if the arr neds to be resized. If it dose not need to be rezised return'''
        if self.size >= self.capacity:
            self.capacity *= 2
            tempArr = [None] * self.capacity

            for i in range(0, self.size):
                tempArr[i] = self.arr[i]
            self.arr = tempArr
        return None

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        self.check_index_out_of_bounds(index, self.size)
        for i in range(0, self.size):
            if i >= index:
                self.arr[i] = self.arr[i + 1]
        self.size -= 1

    # Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0
        self.arr = [None] * self.capacity

    def check_order(self):
        ''' Checks id=f the list is orderd'''
        for i in range(0, self.size):
            if self.arr[i] <= self.arr[i + i]:
                continue
            self.ordered = False

    # Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        # if value at i is grater than value incert the value
        for i in range(0, self.size):
            pass

        self.check_order()

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        if self.check_order():
            self.binary_search(self.arr, 0, self.size, value)
        else:
            self.linear_search(self.arr, value)

    # Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        self.check_empty()
        index = self.find(value)
        self.remove_at(index)

    def check_index_out_of_bounds(self, index, check_size):
        if index > check_size:
            raise IndexOutOfBounds()
        return True

    def check_empty(self, size):
        if size < 1:
            raise Empty()

    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2

            if arr[mid] == x:
                return mid, x

            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return 0

    def linear_search(self, li, x):
        if not li:
            return False
        elif li[0] == x:
            print(x)
        else:
            return self.linear_search(li[1:], x)


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()

    print(arr_lis)
