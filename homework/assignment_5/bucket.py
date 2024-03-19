from exeptions import ItemExistsException, NotFoundException


class Node:
    def __init__(self, key=None, data=None, next=None) -> None:
        self.key = key
        self.data = data
        self.next = next


class Bucket:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert(self, key, data):
        """Inserts an item into the bucket
        - If the item exists already a ItemExistsException is raised
        """
        head = self.head

        while head:
            if head.key == key:
                raise ItemExistsException

            head = head.next

        new_node = Node(key, data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def update(self, key, data):
        """Updates an item in the bucket
        - If the item is not found it raiese a item not found exeption
        """
        head = self.head

        while head:
            if head.key == key:
                head.data = data
                return

            head = head.next

        raise NotFoundException

    def find(self, key):
        """Finds the value in the bucket and returns its value"""
        head = self.head

        if head is None:
            raise NotFoundException

        while head:
            if head.key == key:
                return head.data

            head = head.next
        raise NotFoundException

    def contains(self, key):
        """Checks if the bucket containts a value
        - Returns true if the value is in the bucket
        - Returns false if the value is not in the bucket
        - If no item is found return NotFoundException exeption
        """
        try:
            self.find(key)
            return True
        except NotFoundException:
            return False

    def remove(self, key):
        """Removes a node
        - If a node is the first node set head to head.next
        - Else set previus node next to head next
        - If no node is found rais an exeption
        """

        if self.head.key == key:
            self.head = self.head.next
            self.size -= 1
            return

        previous_node = self.head
        head = previous_node.next

        while head:
            if head.key == key:
                previous_node.next = head.next
                self.size -= 1
                return
            previous_node = head
            head = head.next

        raise NotFoundException

    def __setitem__(self, key, data):
        """Overwrite to allow for the sytax ssl[​key​] = data
        - If a item is in the bucket update its value
        - Else add the item to the colection
        """
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        """Overwrite to allow for the sytax my_var = ssl[​key​]
        - Retruns the data value
        - Else raises a NotFoundException
        """
        return self.find(key)

    def __len__(self):
        """Returns the length of the bucket"""
        return self.size

    def __str__(self) -> str:
        str_out = ""
        current_head = self.head
        while current_head is not None:
            str_out += f"{current_head.data} "
            current_head = current_head.next
        return str_out.strip()


# bucket = Bucket()

# bucket.insert("key1", "data1")
# bucket.remove("key1")
# try:
#     bucket.find("key1")
# except NotFoundException:
#     print("item not found")
