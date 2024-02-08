class IndexOutOfBounds(Exception):
    pass


class NotFound(Exception):
    pass


class Empty(Exception):
    pass


class NotOrdered(Exception):
    pass


class ArrayList:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.ordered = True

    def __str__(self) -> str:
        display = ""

        for i in range(self.size):
            # if i dose not equal the size - 1
            # e.g. the last element

            if i == self.size - 1:
                display += f"{self.arr[i]}"
            else:
                display += f"{self.arr[i]}, "
        return display

    def prepend(self, value):
        self.resize()
        self.insert(value, 0)

    def insert(self, value, index):
        if index > self.size or index < 0:
            raise IndexOutOfBounds()
        self.resize()

        for i in range(self.size, index - 1, -1):
            if i == index:
                self.arr[i] = value
                break
            self.arr[i] = self.arr[i - 1]

        self.size += 1
        self.ordered = False

    def append(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1
        self.ordered = False

    def set_at(self, value, index):
        if index < 0 or index > self.size - 1:
            raise IndexOutOfBounds()

        for i in range(self.size):
            if i == index:
                self.arr[i] = value

    def get_first(self):
        if self.size == 0:
            raise Empty()
        return self.arr[0]

    def get_at(self, index):
        if self.size == 0:
            raise IndexOutOfBounds()
        else:
            if index < 0 or index >= self.size:
                raise IndexOutOfBounds()
            else:
                return self.arr[index]

    def get_last(self):
        if self.size == 0:
            raise Empty()
        return self.arr[self.size - 1]

    def resize(self):
        """Checks if the arr needs to be resized. If it dose not need to be rezised return"""
        if self.size >= self.capacity:
            self.capacity *= 2
            tempArr = [None] * self.capacity

            for i in range(0, self.size):
                tempArr[i] = self.arr[i]
            self.arr = tempArr
        return None

    def remove_at(self, index):
        if index > self.size - 1 or index < 0:
            raise IndexOutOfBounds()
        if self.size > 0:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i + 1]

            self.size -= 1
        return self.arr

    def clear(self):
        self.size = 0
        self.capacity = 4
        self.arr = [None] * self.capacity

    def insert_ordered(self, value):
        if self.ordered is False and self.size > 1:
            raise NotOrdered()

        for i in range(self.size):
            if self.arr[i] > value:
                self.insert(value, i)
                self.ordered = True
                break
            else:
                continue
        return self.arr

    def find(self, value):
        if self.size == 0:
            return None
        if self.ordered:
            self.binary_search(self.arr, 0, self.size - 1, value)
        else:
            self.linear_search(self.arr, value)

    def remove_value(self, value):
        if self.size == 0:
            return None

        index = self.find(value)
        if index > self.size:
            raise NotFound()
        self.remove_at(index)

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
            raise NotFound()

    def linear_search(self, li, val):
        if not li:
            raise NotFound()
        elif li[0] == val:
            return val
        else:
            return self.linear_search(li[1:], val)


if __name__ == "__main__":
    my_arr = ArrayList()

    # my_arr.insert(1, 0)
    # my_arr.insert(2, 1)
    # my_arr.insert(5, 2)
    # my_arr.insert(8, 3)
    # my_arr.append(10)
    # my_arr.append(13)
    # my_arr.append(20)
    # my_arr.append(24)
    # my_arr.insert_ordered(15)
    # my_arr.get_at(2)

    print(my_arr)
