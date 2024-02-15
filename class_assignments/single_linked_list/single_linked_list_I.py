class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        return self.head

    def _print_linked_list_recursive(self, node):
        if node is None:
            return print()
        else:
            print(node.data, end=" ")
            return self._print_linked_list_recursive(node.next)

    def print_linked_list_recursive(self):
        return self._print_linked_list_recursive(self.head)

    def print_linked_list_iterative(self):
        current_head = self.head
        while current_head is not None:
            print(current_head.data)
            current_head = current_head.next

    def remove_head(self):
        self.head = self.head.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def remove_tail(self):
        if self.head is None:
            return None

        if not self.head.next:
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        # if the curent hed is second to last set it to None
        # else move the curent hed


if __name__ == "__main__":
    link1 = Linked_list()

    link1.add_to_head(12)
    link1.add_to_head(1)
    link1.add_to_head(3)

    link1.print_linked_list_recursive()
    # link1.print_linked_list_iterative()
    link1.remove_head()
    link1.append(45)
    link1.append(45)
    link1.print_linked_list_recursive()
    link1.remove_tail()
    link1.print_linked_list_recursive()


# print(h2.next.next.data)
# print_linked_list_recursive(h4)
