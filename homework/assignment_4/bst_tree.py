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
        """The recursive helper function for insert
        - If the value is less than the value of the current node the helper funciton gets called recursively with node left.
        - If the value is grater than the value of the current node the helper funciton gets called recursively with node right.
        If the node has reached a node that is none it adds the new node.
        - If the key of the node being added already exists in the tree and the node is not none and error gets raised and the node is not added.
        """
        if node is None:
            self.size += 1
            return Node(key, data)
        elif key < node.key:
            node.left = self.__insert_recur(node.left, key, data)
        elif key > node.key:
            node.right = self.__insert_recur(node.right, key, data)
        else:
            raise ItemExistsException()

        return node

    def insert(self, key, data) -> None:
        """The function inserts a ndoe to the bst map."""
        self.root = self.__insert_recur(self.root, key, data)

    def __update_recur(self, node, key, data):
        """The recursive helper function for update
        - If the node is none it means the value was not found and an error gets raised.
        - If the key is less than the current node go left.
        - If the key is grater than the current node go right.
        - If the key is found update the value.
        """
        if node is None:
            raise NotFoundException()

        elif key < node.key:
            return self.__update_recur(node.left, key, data)

        elif key > node.key:
            return self.__update_recur(node.right, key, data)
        else:
            node.data = data

    def update(self, key, data) -> None:
        """The function  updates the value of a node if the node is found."""
        self.__update_recur(self.root, key, data)

    def __find_recur(self, node, key):
        """A general recursive helper function that finds
        the node assosiated with the entered if it exist, raises and error othervice.
        - If the node is not found the function raises an erro
        - If the key is less than the current node go left.
        - If the key is grater than the current node go right.
        If the node is found it will retun the node.
        """
        if node is None:
            raise NotFoundException()
        elif key < node.key:
            return self.__find_recur(node.left, key)
        elif key > node.key:
            return self.__find_recur(node.right, key)
        else:
            return node

    def find(self, key) -> None:
        """The function finds the node and returns the data if it exist."""
        node = self.__find_recur(self.root, key)
        return node.data

    def contains(self, key) -> bool:
        """The function returns True if the node exists in the tree and fall otherwise."""
        try:
            self.__find_recur(self.root, key)
            return True
        except NotFoundException:
            return False

    def __swap_remove_left_most_node(self, node, node_to_delete):
        """Removes the node that is the left most node in the right sub tree.
        - Sets the data and key of the node that will be replaced to the node being passed into the function."""
        if node_to_delete.left is None:
            node.key = node_to_delete.key
            node.data = node_to_delete.data
            node.right = self.__remove_node(node_to_delete)
            return node
        else:
            node_to_delete.left = self.__swap_remove_left_most_node(
                node, node_to_delete.left
            )
            return node_to_delete

    def __remove_node(self, node):
        """Removes the node
        - If both left and right are none then just remove the node
        - If left is none return the right node
        - If  right is none retunr left node
        - If node has two child node call the swap and remove leftmost
        """
        if node.left is None and node.right is None:
            return None
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            return self.__swap_remove_left_most_node(node, node.right)

    def __remove_recur(self, node, key):
        """The function finds the node that should be removed.
        - If the node is not found it raises an error
        - If the key is less than the node.key go left
        - If the key is more than the node.key go right
        - If the key is found the __remove_node function is called. It checks for the following
          conditions.
        -       If both left and right are none then just remove the node
        -       If left is none return the right node
        -       If  right is none retunr left node
        -       If node has two child node call the swap and remove leftmost
        """
        if node is None:
            raise NotFoundException()
        elif key < node.key:
            node.left = self.__remove_recur(node.left, key)
        elif key > node.key:
            node.right = self.__remove_recur(node.right, key)
        else:
            self.size -= 1
            return self.__remove_node(node)
        return node

    def remove(self, key) -> None:
        """A function that removes a node."""
        self.root = self.__remove_recur(self.root, key)

    def __setitem__(self, key, data) -> None:
        """The function dose a overwrite for the use of some_bst_map[key] = data syntax.
        - The function relise on the error from the __update function to trigger the following
        -   If the node is found it updates its value.
        -   Else it adds the node to the BST map.
        """
        try:
            self.__update_recur(self.root, key, data)
        except NotFoundException:
            self.__insert_recur(self.root, key, data)
            self.size += 1

    def __getitem__(self, key) -> None:
        """The function allows for the use of
        my_data = some_bst_map[key] syntax.
        - Returns the value of the node. Raises an erro otherwise.
        """
        return self.find(key)

    def __len__(self) -> int:
        """Overwrites the default len method and returns the size of the BST map."""
        return self.size

    def __print_preorder(self, node):
        """The recursive helper function for the __str__ function.
        - Prints the content of the tree inorder.
        """
        output = ""
        if node is not None:
            output += self.__print_preorder(node.left)
            output += f"{{{node.key}: {node.data}}} "
            output += self.__print_preorder(node.right)

        if output == " ":
            return f"The tree has {self.size} items."
        return output

    def __str__(self) -> str:
        """Returns a string with the items printed in order on the format {key: value}"""
        ret_val = self.__print_preorder(self.root)
        return ret_val.strip()
