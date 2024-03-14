class Node:
    def __init__(self, key=None, data=None, next=None) -> None:
        self.key = key
        self.data = data
        self.next = next


class SLL_Map:
    def __init__(self) -> None:
        self.head = None

    def insert(self, key, data):
        self.head = Node(key, data, self.head)
        return self.head

    def find(self, key):
        current = self.head

        while current.key != key and current.next is not None:
            current = current.next

        if current.next is None:
            return None
        else:
            return current.data

    def remove(self, key):
        current = self.head

        if current is None:
            return None

        if current.key == key:
            self.head = current.next

        else:
            while current.next.key != key:
                current = current.next

            current.next = current.next.next

    def __str__(self) -> str:
        str_output = ""

        current = self.head
        while current is not None:
            str_output += f"{current.data}, "
            current = current.next
        return str_output.strip()


if __name__ == "__main__":
    ms = SLL_Map()

    ms.insert(2, "two")
    ms.insert(3, "three")
    ms.insert(5, "five")
    ms.insert(7, "seven")

    ms.remove(2)
    ms.remove(3)
    ms.remove(7)
    ms.remove(5)
    print(ms)
