class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next


class DDL_posList:
    def __init__(self) -> None:
        self.head = Node()
        self.trailer = Node()

        self.head.next = self.trailer
        self.trailer.prev = self.head

        self.current_node = self.trailer

    def insert(self, data) -> None:
        """Inserts a new node on the DDL"""
        new_node = Node(data)

        self.current_node.prev.next = new_node
        new_node.prev = self.current_node.prev
        new_node.next = self.current_node
        self.current_node.prev = new_node

        # sets the current node to new_node
        self.current_node = new_node

    def __str__(self) -> str:
        ret_str = ""

        if self.head.next == self.trailer:
            ret_str = "List is empty"
        else:
            current = self.head.next
            while current != self.trailer:
                ret_str += f"{current.data} "
                current = current.next

        return ret_str.strip()

    def print_revers(self):
        if self.head.next == self.trailer:
            print("List is empty")
        else:
            current = self.trailer.prev
            while current != self.head:
                print(f"{current.data} ", end="")
                current = current.prev
            print("\n")

    def _get_size(self, curr):
        if curr == self.trailer:
            return 0
        return self._get_size(curr.next) + 1

    def get_size(self):
        if self.head.next == self.trailer:
            return None
        else:
            current = self.head.next
            return self._get_size(current)

    def move_to_next(self) -> None:
        if self.current_node.next == self.trailer:
            return None
        self.current_node = self.current_node.next

    def move_to_prev(self) -> None:
        if self.current_node.prev == self.head:
            return None
        self.current_node = self.current_node.prev

    def get_value(self) -> str:
        if self.current_node == self.trailer or self.current_node == self.head:
            return None
        else:
            return self.current_node.data

    def remove(self) -> None:
        if self.head.next == self.trailer:
            print("List is empty")
        elif (
            self.current_node.prev == self.head
            and self.current_node.next == self.trailer
        ):
            self.head.next = self.trailer
            self.trailer.prev = self.head

            self.current_node = self.trailer
        else:
            self.current_node = self.current_node.next
            self.current_node.prev = self.current_node.prev.prev
            self.current_node.prev.next = self.current_node


if __name__ == "__main__":
    ddl = DDL_posList()
    ddl1 = DDL_posList()

    # empty priunt
    print(ddl)

    # insert
    ddl.insert("A")
    ddl.insert("B")
    ddl.insert("C")
    print(ddl)
    ddl.print_revers()
    print(ddl.get_value())

    print(ddl.get_size())

    # move tests
    ddl1.insert("a")
    ddl1.insert("b")
    ddl1.move_to_next()
    ddl1.insert("c")
    ddl1.move_to_prev()
    ddl1.insert("d")
    print(ddl1)

    # test remove
    print(ddl)
    ddl.remove()
    print(ddl)
    ddl.remove()
    print(ddl)
    ddl.remove()
    print(ddl)
