class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []


class General_tree:
    def __init__(self) -> None:
        self.root = None

    def __populate_general_tree_recursiv(self, level=0):
        """The recusive function to populates a general tree.

        - While true add a value to the binary tree.
        - Add the node to the child list.
        - If the value is not numeric or is les then 0 brake from the loop.
        """

        while True:
            value = input("Enter a value: ")
            if not value.isnumeric() or value < 0:
                break

            new_node = Node(value)

            level += 1
            new_node.children.append(self.__populate_general_tree_recursiv(level))

        return None

    def populate_general_tree(self):
        """Populate a general tree."""
        print("ROOT")
        self.root = self.__populate_general_tree_recursiv()

    def __print_postorder_revursive(self, node):
        """Print postorder revursive PPR
        - Print the nodes recursive using post order
        - if the node has a child node loop over all it's
          children calling the PPR there by printing its children
        """

        for child in node.childre:
            self.__print_postorder_revursive(child)

        print(node.data)

    def print_postorder(self):
        """print postorder"""
        self.__print_postorder_revursive(self.root)
        print()

    def __count_occurance_recursive(self, node, value):
        """Count ocurances of """
        count = 0

        if node.data == value:
            count += 1

        for child in node.childre:
            count += self.__count_occurance_recursive(child, value)

        return count

    def count_occurance(self, value=None):
        if value is None:
            return
        else:
            occurances = self.__count_occurance_recursive(self.root, value)
            return occurances

    

    def replace_value(self, value=None, replace_value=None):
        pass


if __name__ == "__main__":
    pass
