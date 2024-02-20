class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 4
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
            self.capacity / 4
        else:
            return True

    def push(self, value):
        self.resize()
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        self.size -= 1
        self.resize()
        return self.arr[self.size - 1]


if __name__ == "__main__":
    m_stack = Stack()
    m_stack.push(1)
    m_stack.push(2)
    m_stack.push(3)
    m_stack.push(5)
    m_stack.push(11)
    m_stack.pop()

    print(m_stack)
