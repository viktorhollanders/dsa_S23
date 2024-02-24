class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DLL_Deque:
    def __init__(self) -> None:
        self.sentinal = Node()

        self.sentinal.next = self.sentinal
        self.sentinal.prev = self.sentinal

    def add_front(self, data):
        new_node = Node(data)

        self.sentinal.next.prev = new_node
        new_node.next = self.sentinal.next
        new_node.prev = self.sentinal
        self.sentinal.next = new_node

    def get_front(self):
        if self.sentinal.next == self.sentinal:
            return None
        return self.sentinal.next.data

    def remove_front(self):
        if self.sentinal.next == self.sentinal:
            return None

        data = self.sentinal.next.data

        self.sentinal.next = self.sentinal.next.next
        self.sentinal.next.prev = self.sentinal
        return data

    def add_back(self, data):
        new_node = Node(data)

        self.sentinal.prev.next = new_node  # from second to last node
        new_node.prev = self.sentinal.prev
        new_node.next = self.sentinal
        self.sentinal.prev = new_node

    def get_back(self):
        if self.sentinal.prev == self.sentinal:
            return None
        return self.sentinal.prev.data

    def remove_back(self):
        if not self.sentinal.prev:
            return None

        data = self.sentinal.prev.data

        self.sentinal.prev = self.sentinal.prev.prev
        self.sentinal.prev.next = self.sentinal
        return data

    def __str__(self) -> str:
        ret_str = ""

        current = self.sentinal.next
        while current != self.sentinal:
            ret_str += f"{current.data} "
            current = current.next

        return ret_str.strip()

    def _get_size(self, current_node):
        if current_node.next == self.sentinal:
            return 0
        return self._get_size(current_node.next) + 1

    def get_size(self):
        start_node = self.sentinal.next
        return self._get_size(start_node)

    def reverse_ddl(self):
        ret_str = ""

        current = self.sentinal.prev
        while current != self.sentinal:
            ret_str += f"{current.data} "
            current = current.prev
        return ret_str.strip()


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
    print(ddl)
    print(ddl.reverse_ddl())
    print("\n")
