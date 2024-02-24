class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")


def get_size(head):
    """Gets the size of the linked list using recursion

    - if the head is not none we make the recursive call and add 1 to the result
    - If the head is none it eather menes that the list is empty in which case it will return 0
    - Or that the last element has been reached and the function will pop the elements from the stack
    finaly returning the result
    """
    if head is None:
        return 0
    else:
        return get_size(head.next) + 1


def reverse_list(head):
    """A function that reverses a single linked list

    - Asumes that the list is in its original order
    - Ones we hit the second to last element we set the next node to that to the new head
    - when we reach the last element of the original head we set the next element
    to None
    - As the recursion unwinds, reverses the pointers to reverse the list.
    """
    if head is None or head.next is None:
        return head

    rest = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return rest


def palindrome(head):
    """A function that checks if the a liked list contains a palindrome

    - start by walking down to the tail of the lsit
    - then compare the head and the tail of the linked list.
    - if they ever return false. it wil be set in the first walue fo the tuple.
    - since this is checked in the if check it will always return false there after ensuring that we get a falsy value
    - The same goes for the true conditon
    """

    def check_for_palindrome(current_head, tail):
        # Walk down the linked list until we reach the end
        if tail is None:
            return True, current_head
        # compare the curent head to the next tail
        is_pal, current_head_comparison = check_for_palindrome(current_head, tail.next)
        # if the is_pall is false of the curent head is not equal to the tail the return value is
        # dwwiched to false
        if not is_pal or current_head_comparison.data != tail.data:
            return False, current_head_comparison
        # else the compasriosn from curent head was true and it gets moved by one and it retuns true
        return True, current_head_comparison.next

    # here we pass in the head twice and walk the second one all the way down to get the tail
    # the second value is a throw away value which we dont need.
    # the true false is stored in the result and that is what is returned from the function
    result, _ = check_for_palindrome(head, head)
    return result


if __name__ == "__main__":
    ##
    print("GET_SIZE TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = None
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", None)
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    print("\n")
    head = Node("A", Node("C", None))
    print_to_screen(head)
    print("size: " + str(get_size(head)))
    print_to_screen(head)

    ##
    print("REVERSE TESTS")
    print("\n")
    head = Node("A", Node("B", Node("C", Node("D", Node("E", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("A", Node("A", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", Node("A", Node("B", Node("A", None)))))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", None)
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = None
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    print("\n")
    head = Node("C", Node("B", None))
    print_to_screen(head)
    rev_head = reverse_list(head)
    print_to_screen(rev_head)

    ##
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("A", Node("E", Node("L", Node("B", Node("A", None)))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("L", Node("A", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")

    head = Node("C", Node("A", Node("L", Node("T", Node("E", Node("C", None))))))
    print_to_screen(head)
    print(palindrome(head))
    print_to_screen(head)

    print("\n")
