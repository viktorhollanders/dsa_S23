class Node:
    def __init__(self, data=None, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class ItemExistsException(Exception):
    pass


class BST:
    def __init__(self) -> None:
        self.root = None

    def __insert_recur(self, node, key, data):
        if node is None:
            return Node(key, data)

        if key < node.key:
            node.left = self.__insert_recur(node.left, key, data)
            return node

        if key > node.key:
            node.right = self.__insert_recur(node.right, key, data)
            return node

        if node is not None and node.key == key:
            raise ItemExistsException("Item already exists")
        return node

    def insert(self, key, data):
        self.__insert_recur(self.root, key, data)

    def __size_recur(self, node):
        if node is None:
            return 0

        node_left = self.__get_length(node.left)
        node_right = self.__get_length(node.right)

        return node_left + node_right + 1

        # can be written as
        # return self.__get_length(node.left) + self.__get_length(node.right) + 1

    def size(self):
        return self.__size_recur(self.root)
