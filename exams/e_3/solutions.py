class GeneralTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.children = []


class GeneralTree:
    def __init__(self):
        # this tree will be used in tests but your code must work for other tree setups as well
        self.root = GeneralTreeNode(7)
        root_child_1 = GeneralTreeNode(2)
        root_child_2 = GeneralTreeNode(1)
        root_child_3 = GeneralTreeNode(9)
        self.root.children = [root_child_1, root_child_2, root_child_3]
        root_grandchild_1 = GeneralTreeNode(13)
        root_grandchild_2 = GeneralTreeNode(4)
        root_grandchild_3 = GeneralTreeNode(2)
        root_grandchild_4 = GeneralTreeNode(6)
        root_grandchild_5 = GeneralTreeNode(1)
        root_grandchild_6 = GeneralTreeNode(8)
        root_grandchild_7 = GeneralTreeNode(15)
        root_grandchild_8 = GeneralTreeNode(5)
        self.root.children[0].children = [root_grandchild_1]
        self.root.children[1].children = [
            root_grandchild_2,
            root_grandchild_3,
            root_grandchild_4,
            root_grandchild_5,
        ]
        self.root.children[2].children = [
            root_grandchild_6,
            root_grandchild_7,
            root_grandchild_8,
        ]

    def find_smallest_helper(self, node):
        smallest = node.data

        for child in node.children:
            if child.data < smallest:
                smallest = min(smallest, self.find_smallest_helper(child))

        return smallest

    def find_smallest(self):
        return self.find_smallest_helper(self.root)

    def sum_trees_helper(self, node):
        count = node.data

        for child in node.children:
            count += self.sum_trees_helper(child)

        return count

    def sum_tree(self):
        return self.sum_trees_helper(self.root)

    def odd_numbers_helper(self, node):
        odds_list = [node.data] if node.data % 2 == 1 else []

        for child in node.children:
            odds_list.extend(self.odd_numbers_helper(child))

        return odds_list

    def odd_numbers(self):
        return self.odd_numbers_helper(self.root)


if __name__ == "__main__":
    print("Testing find_smallest")
    tree = GeneralTree()
    print(tree.find_smallest())
    print("Testing sum_tree")
    tree = GeneralTree()
    print(tree.sum_tree())
    print("Testing odd_numbers")
    tree = GeneralTree()
    print(sorted(tree.odd_numbers()))
