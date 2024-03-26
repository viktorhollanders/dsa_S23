from bucket import Bucket
from exeptions import NotFoundException


class HashMap:
    def __init__(self) -> None:
        self.capacity = 10
        self.size = 0
        self.arr = [Bucket() for _ in range(self.capacity)]

    def rebuild(self):
        if self.size >= 1.2 * self.capacity:
            new_capacity = self.capacity * 2
            temp_arr = [Bucket() for _ in range(new_capacity)]

            for item in self.arr:
                if item.key:
                    temp_arr[item] = self.arr[item]

            self.arr = temp_arr
            self.capacity = new_capacity

    def insert(self, key, data):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity

        self.arr[compressed_hash].insert(key, data)
        self.size += 1

    def update(self, key, data):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity

        self.arr[compressed_hash].update(key, data)

    def find(self, key):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity

        if (
            self.arr[compressed_hash].head is None
            or self.arr[compressed_hash].head.key != key
        ):
            raise NotFoundException

        return self.arr[compressed_hash].find(key)

    def contains(self, key):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity
        if self.arr[compressed_hash].contains(key):
            return True
        return False

    def remove(self, key):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity
        self.arr[compressed_hash].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        hash_key = hash(key)
        compressed_hash = hash_key % self.capacity

        self.arr[compressed_hash].__setitem__(key, data)
        self.size += 1

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size
