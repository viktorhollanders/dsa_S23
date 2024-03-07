from exeptions import ItemExistsException, NotFoundException


class Node:
    def __init__(self, key=None, data=None, left=None, right=None) -> None:
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BSTMap:
    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __insert_recur(self, node, key, data):
        try:
            if node is None:
                return Node(key, data)

            if key < node.key:
                node.left = self.__insert_recur(node.left, key, data)
                return node

            if key > node.key:
                node.right = self.__insert_recur(node.right, key, data)
                return node

            self.size += 1
            return node
        except ItemExistsException:
            print("error")

    def insert(self, key, data):
        self.root = self.__insert_recur(self.root, key, data)

    def __update_recur(self, node, key, data):
        try:
            if node == key:
                node = node.data
                return node

            if key < node.key:
                node.left = self.__insert_recur(node.left, key, data)
                return node

            if key > node.key:
                node.right = self.__insert_recur(node.right, key, data)
                return node

            return node
        except FileNotFoundError:
            print("error")

    def update(self, key, data):
        self.root = self.__update_recur(self.root, key, data)

    def __find_recur(self, node, key):
        try:
            if key == node:
                return node.data

            if key < node.key:
                node.left = self.__insert_recur(node.left, key)
                return node

            if key > node.key:
                node.right = self.__insert_recur(node.right, key)
                return node

            return node

        except FileNotFoundError:
            print("error")

    def find(self, key):
        self.root = self.__find_recur(self.root, key)

    def __contains_recur(self, node, key):
        if key is None:
            return False

        if key < node.key:
            node.left = self.__insert_recur(node.left, key)
            return node

        if key > node.key:
            node.right = self.__insert_recur(node.right, key)
            return node

        return True

    def contains(self, key):
        self.root = self.__contains_recur(self.root, key)

    def __swap_remove_left_most(self, original_node, node):
        if node is None or node.left is None:
            return self.__swap_remove_left_most(original_node, node.left)
        else:
            original_node = node.data
            return self.__remove_node(node)

    def __remove_node(self, node):
        if node.left is None and node.right is None:
            return None
        elif node.right is None:
            return node.left
        elif node.left is None:
            return node.right
        else:
            node.right = self.__swap_remove_left_most(node, node.right)

    def __remove_recur(self, node, key):
        try:
            if key == node:
                return self.__remove_node(node)

            if key < node.key:
                node.left = self.__insert_recur(node.left, key)
                return node

            if key > node.key:
                node.right = self.__insert_recur(node.right, key)
                return node

            self.size -= 1
            return node
        except NotFoundException:
            print("error")

    def remove(self, key):
        self.root = self.__remove_recur(self.root, key)

    def __setitem__(self, key, data):
        # If equal ​key​ is already in the collection, update its ​data​ value
        if self.insert(key, data):

        #   Otherwise add the value pair to the collection

        pass

    def __getitem__(self, key):
        pass

    def __len__(self):
        pass

    def __str__(self):
        pass
