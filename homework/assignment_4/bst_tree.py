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
        try:
            self.root = self.__insert_recur(self.root, key, data)
        except ItemExistsException as e:
            print(e)

    def __update_recur(self, node, key, data):
        if node is None:
            raise NotFoundException("Item not found")

        if key < node.key:
            node.left = self.__update_recur(node.left, key, data)
            return node

        if key > node.key:
            node.right = self.__update_recur(node.right, key, data)
            return node

        node.data = data
        return node

    def update(self, key, data):
        try:
            return self.__update_recur(self.root, key, data)
        except NotFoundException as e:
            print(e)

    def __print_preorder(self, node):
        output = ""
        if node is not None:
            output += self.__print_preorder(node.left)
            output += f"{{{node.key}: {node.data}}} "
            output += self.__print_preorder(node.right)

        return output

    def __str__(self) -> str:
        return self.__print_preorder(self.root)

    def __find_recur(self, node, key):
        if node is None:
            raise NotFoundException("Item not found")
        if key == node.key:
            return node

        if key < node.key:
            node = self.__find_recur(node.left, key)
            return node

        if key > node.key:
            node = self.__find_recur(node.right, key)
            return node

        return node

    def find(self, key):
        try:
            node = self.__find_recur(self.root, key)
            print(node.data)
        except NotFoundException as e:
            print(e)

    def contains(self, key):
        try:
            self.__find_recur(self.root, key)
            return True
        except NotFoundException:
            return False


m = BSTMap()
m.insert(5, "five")
m.insert(3, "three")
m.insert(7, "seven")
# print(m)
# m.update(3, "hello")
# print(m)
m.find(3)
print(m.contains(10))
