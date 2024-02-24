class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # front = head
    def push_front(self, data):
        """Pushes from the front of the linkes list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return self.head

        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return self.head

    def pop_front(self):
        """Removes a node from the front of the list
        - Returns the value of the node that was removed of
        """
        if self.head is None:
            return self.head

        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    # Back = tail
    def push_back(self, data):
        """Adds a new node to the back of the linked list
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def pop_back(self):
        """Removes a node from  the back of the linked list
        - Returns the value of the node that was removed of
        """
        if self.head is None:
            return None

        if not self.head.next:
            data = self.head.data
            self.head = None
            self.tail = self.head
            self.size -= 1
            return data

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        data = current_node.next.data
        current_node.next = None
        self.tail = current_node
        self.size -= 1
        return data

    def get_size(self):
        """Gets the size of the linked list
        """
        return self.size

    def __str__(self):
        ret_linked_list = ""
        current = self.head
        while current is not None:
            data = current.data
            ret_linked_list += f"{data} "
            current = current.next

        return ret_linked_list.strip()
