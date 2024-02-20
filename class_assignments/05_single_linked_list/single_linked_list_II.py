class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


head_a = None
head_b = None


def add_node(data, head):
    """Adds a node to the linked list

    Sets the new node to a instance of the node class and adds it
    to the linkde list.
    """
    new_node = Node(data, head)
    head = new_node
    return head


def print_linked_list(node):
    """Prints a linde list

    Takes in the head of the current list and prints all its elements.
    """
    if node is None:
        return print()
    else:
        print(node.data, end=" ")
        return print_linked_list(node.next)


def length_of_list(node):
    """Prints the length of the linked list."""
    if node is None:
        return 0
    else:
        return length_of_list(node.next) + 1


def insert_orderd(node, data):
    """Inserts a value in a orderd linked list.

    The function takes in a node, the data we want to insert, and the previous node.
    """
    if data < node.data:
        new_node = Node(data, node.next)
        node.next = new_node
    else:
        return insert_orderd(node.next, data)


def reverse_linked_list(head):
    """Returns the linked list in revers order"""

    if head is None or head.next is None:
        return head

    rest = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return rest


def merge_lists(node_a, node_b):

    pass


def merge_sort():
    pass


if __name__ == "__main__":
    # head_a
    n0 = add_node("1", head_a)
    n1 = add_node("2", n0)
    n2 = add_node("4", n1)
    n3 = add_node("7", n2)
    n4 = add_node("9", n3)

    # head_b
    m0 = add_node("3", head_b)
    m1 = add_node("5", m0)
    m2 = add_node("6", m1)
    m3 = add_node("8", m2)
    m4 = add_node("10", m3)

    print_linked_list(n4)
    print_linked_list(m3)

    print(length_of_list(head_a))
    reversed = reverse_linked_list(n4)
    print_linked_list(reversed)
