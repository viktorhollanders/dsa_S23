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
        if node is None:
            return Node(key, data)

        if key < node.key:
            node.left = self.__insert_recur(node.left, key, data)
            return node

        if key > node.key:
            node.right = self.__insert_recur(node.right, key, data)
            return node

        return node

    def insert(self, key, data):
        try:
            self.root = self.__insert_recur(self.root, key, data)
        except None:
            ItemExistsException

    def __update_recur(self, node, key, data):
        try:
            if node.key == key:
                node.dat = data
                return node

            if key < node.key:
                node.left = self.__insert_recur(node.left, key, data)
                return node

            if key > node.key:
                node.right = self.__insert_recur(node.right, key, data)
                return node

            return node
        except NotFoundException:
            print("error")

    def update(self, key, data):
        self.root = self.__update_recur(self.root, key, data)

    def __find_recur(self, node, key):
        try:
            if key == node.key:
                return node.data

            if key < node.key:
                node.left = self.__find_recur(node.left, key)
                return node

            if key > node.key:
                node.right = self.__find_recur(node.right, key)
                return node

            return node

        except FileNotFoundError:
            print("error")

    def find(self, key):
        return self.__find_recur(self.root, key)

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
        return self.__contains_recur(self.root, key)

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
        has_key = self.find(key)

        if has_key:
            self.update(data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        try:
            self.find(key)
        except None:
            NotFoundException

    def __len__(self):
        pass

    def __str__(self):
        pass
