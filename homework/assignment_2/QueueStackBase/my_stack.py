from array_deque import ArrayDeque
from my_linked_list import LinkedList


class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue

        # self.container = LinkedList()

        # The push_back and pop_back from the arrayDequeu are used for the stack since it will make the runtime O(1)
        # To push on a stack the push_back function can be used since what is first in is the first out
        # To pop a stack the pop_back function can be used since what is first in is the first out
        self.container = ArrayDeque()
        pass

    def push(self, data):
        return self.container.push_back(data)

    def pop(self):
        return self.container.pop_back()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return self.container.__str__()
