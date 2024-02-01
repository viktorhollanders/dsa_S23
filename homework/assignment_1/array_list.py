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
        # TODO: remove 'pass' and implement functionality
        self.size = 0
        self.capacity = 5
        self.arr = [None] * self.capacity

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
        # TODO: remove 'pass' and implement functionality
        self.insert(value, 0)

    # Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        for i in range(self.size - 1, index - 1, -1):
            self.arr[i + 1] = self.arr[i]
            if i == index:
                self.arr[index] = value

        self.size += 1

    # Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality

        self.arr[self.size] = value
        self.size += 1

    # Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        # if to big
        # Else pas
        pass

    # Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    # Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    # Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.prepend(23)
    arr_lis.prepend(5)
    #     arr_lis.prepend(2)
    arr_lis.prepend(1)
    # [1, 5, 23]
    arr_lis.insert(3, 1)
    # [1, 3, 5, 23]
    print(str(arr_lis))
