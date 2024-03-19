import unittest

from bucket import Bucket, ItemExistsException, NotFoundException


class TestBucket(unittest.TestCase):
    def setUp(self):
        self.bucket = Bucket()

    def test_insert_and_find(self):
        self.bucket.insert("key1", "data1")
        self.assertEqual(self.bucket.find("key1"), "data1")

    def test_insert_duplicate_key(self):
        self.bucket.insert("key1", "data1")
        with self.assertRaises(ItemExistsException):
            self.bucket.insert("key1", "data2")

    def test_contains(self):
        self.bucket.insert("key1", "data1")
        self.assertTrue(self.bucket.contains("key1"))
        self.assertFalse(self.bucket.contains("key2"))

    def test_remove(self):
        self.bucket.insert("key1", "data1")
        self.bucket.remove("key1")
        with self.assertRaises(NotFoundException):
            self.bucket.find("key1")

    def test_update(self):
        self.bucket.insert("key1", "data1")
        self.bucket.update("key1", "data2")
        self.assertEqual(self.bucket.find("key1"), "data2")

    def test_len(self):
        self.bucket.insert("key1", "data1")
        self.assertEqual(len(self.bucket), 1)


if __name__ == "__main__":
    unittest.main()
