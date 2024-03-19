# Let's create the Python file containing the unit tests for the provided HashMap class and the assumed Bucket class behavior.


import unittest

from hash_map import HashMap
from bucket import NotFoundException


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.hash_map = HashMap()
        self.key_int = 1
        self.key_str = "key"
        self.data_int = 10
        self.data_str = "data"

    def test_init(self):
        self.assertEqual(len(self.hash_map.buckets), 4)
        self.assertEqual(self.hash_map.size, 0)

    def test_insert_and_find(self):
        # Test insert with integer key
        self.hash_map.insert(self.key_int, self.data_int)
        self.assertEqual(self.hash_map.find(self.key_int), self.data_int)
        # Test insert with string key
        self.hash_map.insert(self.key_str, self.data_str)
        self.assertEqual(self.hash_map.find(self.key_str), self.data_str)
        # Test resize through insert
        for i in range(2, 6):  # Inserting more to trigger resize
            self.hash_map.insert(i, f"data_{i}")
        self.assertEqual(len(self.hash_map.buckets), 8)
        self.assertEqual(self.hash_map.size, 6)

    def test_update(self):
        self.hash_map.insert(self.key_int, self.data_int)
        new_data_int = 20
        self.hash_map.update(self.key_int, new_data_int)
        self.assertEqual(self.hash_map.find(self.key_int), new_data_int)

        self.hash_map.insert(self.key_str, self.data_str)
        new_data_str = "new_data"
        self.hash_map.update(self.key_str, new_data_str)
        self.assertEqual(self.hash_map.find(self.key_str), new_data_str)

        # Testing NotFoundException
        with self.assertRaises(NotFoundException):
            self.hash_map.update("non_existing_key", "data")

    def test_contains(self):
        self.hash_map.insert(self.key_int, self.data_int)
        self.assertTrue(self.hash_map.contains(self.key_int))
        self.assertFalse(self.hash_map.contains(2))

    def test_remove(self):
        self.hash_map.insert(self.key_int, self.data_int)
        self.hash_map.remove(self.key_int)
        self.assertFalse(self.hash_map.contains(self.key_int))

        # Testing NotFoundException
        with self.assertRaises(NotFoundException):
            self.hash_map.remove("non_existing_key")

        # Test size after remove
        self.assertEqual(len(self.hash_map.buckets), 4)

    def test_get_bucket_index_and_compress_hash(self):
        # These methods are internal, but we can indirectly test them via insert/find
        self.hash_map.insert(self.key_int, self.data_int)
        found_data = self.hash_map.find(self.key_int)
        self.assertEqual(found_data, self.data_int)

    def test_setitem_getitem_len(self):
        # __setitem__ and __getitem__
        self.hash_map[self.key_int] = self.data_int
        self.assertEqual(self.hash_map[self.key_int], self.data_int)

        # __len__
        self.assertEqual(len(self.hash_map), 1)


if __name__ == "__main__":
    unittest.main()
