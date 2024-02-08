class A_queue:
    def __init__(self) -> None:
        self.capacity = 4
        self.size = 0
        self.arr = [None] * self.capacity

    def __str__(self) -> str:
        return_string = ""

        for i in range(0, self.size):
            if i == self.size - 1:
                return_string += str(self.arr[i])
            else:
                return_string += f"{self.arr[i]}, "

        return return_string

    def resize(self):
        if self.size >= self.capacity:
            self.capacity *= 2
            tempArr = [None] * self.capacity

            for i in range(0, self.size):
                tempArr[i] = self.arr[i]
            self.arr = tempArr
        elif self.capacity / 4 < self.size:
            self.capacity /= 4
        else:
            return True

    def add(self, value):
        self.arr[self.size] = value
        self.size += 1

    def remove(self):
        first_out = self.arr[0]

        for i in range(0, self.size):
            self.arr[i] = self.arr[i + 1]
        self.size - 1
        return first_out


if __name__ == "__main__":
    pass
