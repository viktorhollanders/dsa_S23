class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def palindrome(head):
    def get_tail(tail):
        nonlocal head
        if tail is None:
            return True
        if not tail:
            return False

        comparison = (tail.data == head.data)

        head = head.next
        return comparison

    return get_tail(head)


if __name__ == "__main__":
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))

    print(palindrome(head))

    # print("\n")

    # head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))

    # print(palindrome(head))
    # print_to_screen(head)

    # print("\n")

    # head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    # print_to_screen(head)
    # print(palindrome(head))
    # print_to_screen(head)

    # print("\n")

    # head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    # print_to_screen(head)
    # print(palindrome(head))
    # print_to_screen(head)

    # print("\n")
