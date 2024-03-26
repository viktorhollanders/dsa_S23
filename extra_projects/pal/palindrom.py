class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class IsPalindrome:
    def __init__(self, head) -> None:
        self.current_head = head
        self.tail = head

    def is_palindrome(self, current_head):
        if current_head is None:
            return True, None

        isp, next_node = self.is_palindrome(current_head.next)
        if not isp:
            return False, None

        check_pall = self.current_head.data == next_node.data
        self.current_head = self.current_head.next

        if next_node:
            return check_pall, next_node.next
        else:
            None


def print_to_screen(head):
    if head != None:
        print(head.data, end=" ")
        print_to_screen(head.next)
    else:
        print("")

def palindrome3(head):
    def check_for_palindrome(left, right):
        if right is None:
            return True, left
        is_pal, left_comparing_node = check_for_palindrome(left, right.next)
        if not is_pal or left_comparing_node.data != right.data:
            return False, left_comparing_node
        return True, left_comparing_node.next

    result, _ = check_for_palindrome(head, head)
    return result

def palindrome(head):
    def check_for_palindrome(left, right):
        if right is None:
            return True, left
        is_pal, left_comparing_node = check_for_palindrome(left, right.next)

        #
        if not is_pal or left_comparing_node.data != right.data:
            return False, left_comparing_node
        return True, left_comparing_node.next

    result, _ = check_for_palindrome(head, head)
    return result


# get the tail of the linked list

# On each iteration we move the head the the next node
# becasue of the recursion the tail will move upwards

# compare the current head and the tail on each iteration
#   if the match return True
#   if any of the cases return false keep returning false


if __name__ == "__main__":
    print("PALINDROME TESTS")
    print("\n")
    head = Node("A", Node("E", Node("L", Node("E", Node("A", None)))))

    print_to_screen(head)
    print(palindrome(head))
    # print(palindrome(head)) True / False

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


# F version

# def palindrome(head):
#     def get_tail(tail):
#         nonlocal head
#         if tail is None:
#             return True
#         if not tail:
#             return False

#         comparison = (tail.data == head.data)

#         head = head.next
#         return comparison

#     return get_tail(head)
