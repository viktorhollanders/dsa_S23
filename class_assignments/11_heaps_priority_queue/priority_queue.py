class HeapNode:
    def __init__(self, priority, data=None, parent=None, left=None, right=None) -> None:
        self.priority = priority
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


class PriorityQueue:
    def __init__(self) -> None:
        self.root = None
        self.last_node = None

    def _swap_nodes(self, node):
        if node.parent is None:
            return node
        # If the node is grater than parent node
        parent = node.parent
        if parent.priority > node.priority:
            node.priority, parent.priority = parent.priority, node.priority
            node.data, parent.data = parent.data, node.data
            parent = self._swap_nodes(node)
        return parent

    def _add_helper(self, node, priority, data):
        new_node = HeapNode(priority, data)

        if self.root is None:
            self.last_node = new_node
            return new_node

        if not node.left and not node.right:
            new_node.parent = node
            node.left = new_node
            node = self._swap_nodes(new_node)
            self.last_node = new_node
            return node

        if node.left:
            new_node.parent = node
            node.right = new_node
            node = self._swap_nodes(new_node)
            self.last_node = new_node
            return node

        # set priority
        # refrence to parent
        # set the last node

    def add(self, priority, data):
        self.root = self._add_helper(self.root, priority, data)

    def remove(self):
        node_to_remove = self.root
        return node_to_remove

    def __len__(self):
        pass

    def _str_helper(self, node):
        output = ""

        if node is not None:
            output += self._str_helper(node.right)
            output += f"{node.priority} ,{node.data} "
            output += self._str_helper(node.left)

        return output

    def __str__(self):
        return self._str_helper(self.root).strip()


pq = PriorityQueue()
pq.add(7, "seven")
print(pq.last_node.data)
pq.add(2, "two")
print(pq.last_node.data)
pq.add(1, "one")
print(pq.last_node.data)
# pq.add(8, "eight")
# pq.add(3, "three")
print(pq)
