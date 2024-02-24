from my_linked_list import LinkedList


class Queue:
    def __init__(self):
        # we use the linked list for the queue so everything will be O(1) except for remove and __str__
        # which will be O(n)
        self.container = LinkedList()

    def add(self, data):
        # We use the push_front function to add to a queue since in a queue the first one in is the first one out
        self.container.push_front(data)

    def remove(self):
        # We use the pop_back function to remove from a queue since in a queue the first one in is the first one out
        return self.container.pop_back()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)
