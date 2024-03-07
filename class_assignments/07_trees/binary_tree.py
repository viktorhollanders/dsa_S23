class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def __populate_binary_tree_recursive(self, level=0):
        """The recusive function to populate the binary tree

        - If the value is none, 0, or an escape character return
        - Othervice populate the left side
        - It the leftside is populated populate the right side
        """
        value = input("Enter a value: ")

        if not value.isnumeric() or value < 0:
            return None

        new_node = Node(value)

        level += 1
        print(f"{level * '-----'} LEFT")
        new_node.left = self.__populate_binary_tree_recursive(level)

        print(f"{level * '-----'} RIGHT")
        new_node.right = self.__populate_binary_tree_recursive(level)

        return new_node

    def populate_binary_tree(self):
        """Populates the binary tree."""
        print("ROOT")
        self.root = self.__populate_binary_tree_recursive()

    def __print_preoreder_recursive(self, node):
        """The recursive function for preorder printing of the binary tree"""
        if node is None:
            return
        print(node.data, end=" ")
        self.__print_preoreder_recursive(node.left)
        self.__print_preoreder_recursive(node.right)

    def print_preorder(self):
        """Preorder print"""
        self.__print_preoreder_recursive(self.root)
        print()

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

    def __print_postorder_recursive(self, node):
        """The recursive function for postorder printing of the binary tree"""
        if node is None:
            return

        self.__print_postorder_recursive(node.left)
        self.__print_postorder_recursive(node.right)
        print(node.data, end=" ")

    def postorder_print(self):
        """Postorder print"""
        self.__print_postorder_recursive(self.root)
        print()


if __name__ == "__main__":
    tree = BinaryTree()
    tree.populate_binary_tree()
    tree.print_preorder()
