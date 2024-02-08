class A_queue:
    def __init__(self) -> None:
        self.DEFAULT_CAPASITY = 10
        self.data = [None] * self.DEFAULT_CAPASITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def add(self, value):
        self.data[self.size] = value
        self.size += 1

    def remove(self):
        first_out = self.data[0]

        for i in range(0, self.size):
            self.data[i] = self.data[i + 1]
        self.fron = (self.front + 1) % self.data
        self.size - 1
        return first_out

    def resize(self):
        if self.size >= self.data:
            self.data * 2
            tempArr = [None] * self.data

            for i in range(0, self.size):
                index = i % len(self.data)
                tempArr[i] = self.data[index]
                self.front




if __name__ == "__main__":
    pass
