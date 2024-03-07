class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self) -> None:
        self.root = None

    def __insetrt_recur(self, current, value):
        if current is None:
            return Node(value)

        if value < current.data:
            current.left = self.__insetrt_recur(current.left, value)
            return currentc

        if value > current.data:
            current.right = self.__insetrt_recur(current.right, value)
            return current

        print("already exists")
        return current

    def insert(self, value):
        self.root = self.__insetrt_recur(self.root, value)

    def __find_recur(self, current, value):
        if current.data is None:
            return None

        if value < current.data:
            current.left = self.__insetrt_recur(current.left, value)

        if value > current.data:
            current.right = self.__insetrt_recur(current.right, value)

        return value

    def find(self, value):
        return self.__find_recur(value)

    def __print_inorder_recursive(self, node):
        """The recursive function for inorder printing of the binary tree"""
        if node is None:
            return

        self.__print_inorder_recursive(node.left)
        print(node.data, end=" ")
        self.__print_inorder_recursive(node.right)

    def inorder_print(self):
        """Preorder print"""
        self.__print_inorder_recursive(self.root)
        print()

    def __str__(self) -> str:
        pass


if __name__ == "__main__":
    bst = BST()

    bst.insert(3)
    bst.insert(6)
    bst.insert(2)
    bst.insert(8)
    bst.insert(3)

    bst.inorder_print()
