class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self._head = Node()
        self._trailer = Node()

        self._head.next = self._trailer
        self._trailer.prev = self._head
        self.current_node = self._trailer
        self.size = 0

    def insert(self, data):
        """Inserts a value at the current position in a DLL"""
        if self.current_node != self._head:
            if self.current_node is None:
                self.current_node = self._trailer
            new_node = Node(data, self.current_node.prev, self.current_node)

            self.current_node.prev.next = new_node
            self.current_node.prev = new_node

            self.current_node = new_node
            self.size += 1

    def remove(self):
        """Removes a value form at the current position in a DLL
        - Checks if the curent node's data is not none
        - Moves the current node the the next node
        - Then swapa the nodes
        """
        if (
            self.current_node is not None
            and self.current_node != self._trailer
            and self.current_node != self._head
        ):
            next_node = self.current_node.next
            prev_node = self.current_node.prev

            next_node.prev = prev_node
            prev_node.next = next_node
            self.current_node.next = self.current_node.prev = None
            self.current_node = next_node
            self.size -= 1

    def get_value(self):
        """Gets the value of the current node"""
        if self.current_node is not None:
            return self.current_node.data

    def move_to_next(self):
        """Move to next node
        - If the current node dose not have any data it means it is the head
        """
        if self.current_node != self._trailer:
            self.current_node = self.current_node.next

    def move_to_prev(self):
        """Move to previus node"""
        if self.current_node is not None and self.current_node.prev != self._head:
            self.current_node = self.current_node.prev

    def move_to_pos(self, pos):
        if 0 <= pos <= self.size:
            self.current_node = self._head
            for _ in range(pos + 1):
                self.current_node = self.current_node.next

    def clear(self):
        self._head.next = self._trailer
        self._trailer.prev = self._head
        self.current_node = self._trailer
        self.size = 0

    def get_first_node(self):
        """Gets the first node of the DLL
        - Returns None if the list is empty
        """
        if self.size == 0:
            return None
        return self._head.next

    def get_last_node(self):
        """Gets the last node of the DLL
        - Returns None if the list is empty
        """
        if self.size == 0:
            return None

        return self._trailer.prev

    def partition(self, low, high):
        """Loops from low to high and moves all nodes less than low infront of pivot.
        - Takes in two nodes as parameters.
        - Sets the current node to the pivot onse the function is done.

        The pivot is set to low
        Then we check all notes untill we reach the end (the outer while loop)
        On each iteration we check if:
        - the note being checked is les than the pivot the curent node gets set to pivot
        this is so we can insert infront of the pivot
        - We set the current node to the node being checked to be able to remove the current nodethe
        - We set the cuttent node back to pivot again.
        - This prosess is repeted everytime we hit a node that is les then pivot
        If the node is more than pivot we move on
        """
        pivot = low
        self.current_node = pivot
        if self.size >= 2:
            check_node = self.get_first_node()

            while check_node.next != self._trailer:
                while (
                    check_node.data >= pivot.data and check_node.next != self._trailer
                ):
                    check_node = check_node.next

                if check_node.data < pivot.data:
                    self.current_node = pivot
                    self.insert(check_node.data)
                    self.current_node = check_node
                    self.remove()
                    self.current_node = pivot

                    check_node = pivot

    def sort(self):
        """Sorts the list"""
        if self.size == 1:
            self.current_node = self.get_first_node()
        elif self.size >= 2:
            pivot = self.get_first_node().next
            swap_node = pivot

            # outer loop starts at the second element
            while pivot != self._trailer:
                # inner loop to swap the elements
                while swap_node.prev != self._head:
                    previous_node = swap_node.prev

                    if swap_node.data < previous_node.data:
                        swap_node.data, previous_node.data = (
                            previous_node.data,
                            swap_node.data,
                        )
                    swap_node = swap_node.prev
                pivot = pivot.next
                swap_node = pivot

                self.current_node = self.get_first_node()

    def __len__(self):
        """Returns the lenght of a DLL"""
        return self.size

    def __str__(self):
        """Returns all the values of the DLL"""
        ret_str = ""

        current_node = self._head.next
        while current_node.data is not None:
            ret_str += f"{current_node.data} "
            current_node = current_node.next

        return ret_str.strip()


if __name__ == "__main__":
    # create tests here if you want
    pass
