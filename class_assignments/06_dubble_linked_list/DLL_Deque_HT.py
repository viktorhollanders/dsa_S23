class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DLL_Deque:
    def __init__(self) -> None:
        self.head = Node()
        self.trailer = Node()
        self.head.next = self.trailer
        self.trailer.prev = self.head

    def add_front(self, data):
        new_node = Node(data)

        self.head.next.prev = new_node
        new_node.next = self.head.next

        new_node.prev = self.head
        self.head.next = new_node

    def get_front(self):
        if self.head.next == self.trailer:
            return None
        return self.head.next.data

    def remove_front(self):
        if self.head.next == self.trailer:
            return None

        data = self.head.next.data

        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return data

    def add_back(self, data):
        new_node = Node(data)

        self.trailer.prev.next = new_node  # from second to last node
        new_node.prev = self.trailer.prev
        new_node.next = self.trailer
        self.trailer.prev = new_node

    def get_back(self):
        if self.trailer.prev == self.head:
            return None
        return self.trailer.prev.data

    def remove_back(self):
        if not self.trailer.prev:
            return None

        data = self.trailer.prev.data

        self.trailer.prev = self.trailer.prev.prev
        self.trailer.prev.next = self.trailer
        return data

    def __str__(self) -> str:
        ret_str = ""

        current = self.head.next
        while current != self.trailer:
            ret_str += f"{current.data} "
            current = current.next

        return ret_str.strip()

    def reverse_ddl(self):
        ret_str = ""

        current = self.trailer.prev
        while current != self.head:
            ret_str += f"{current.data} "
            current = current.prev
        return ret_str.strip()

    def _get_size(self, current_node):
        if current_node == self.trailer:
            return 0
        return self._get_size(current_node.next) + 1

    def get_size(self):
        if self.head.next == self.trailer:
            print("list is empty")
        else:
            head = self.head.next
            return self._get_size(head)


if __name__ == "__main__":
    ddl = DLL_Deque()

    # add front
    print("add front")
    ddl.add_front(3)
    ddl.add_front(4)
    ddl.add_front(11)
    ddl.add_front(332)
    print(ddl.get_size())
    print(ddl)
    print("\n")

    # remove front
    print("remove front")
    ddl.remove_front()
    print(ddl.get_size())
    print(ddl)
    print("\n")

    # get front
    print("get front")
    print(ddl)
    print(f"Value at the front is : {str(ddl.get_front())}")
    print("\n")

    # add back
    print("add back")
    ddl.add_back(200)
    ddl.add_back(201)
    print(ddl.get_size())
    print(ddl)
    print("\n")

    # remove back
    print("remove back")
    ddl.remove_back()
    print(ddl.get_size())
    print(ddl)
    print("\n")

    # get back
    print("get back")
    print(ddl)
    print(f"Value at the back is : {str(ddl.get_back())}")
    print("\n")

    # reverse DDL
    print("revers ddl")
    print(ddl.reverse_ddl())
    print("\n")
