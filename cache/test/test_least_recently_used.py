import unittest
from cache.least_recently_used import (db,
                                       get_value,
                                       shuffle_queue,
                                       update_queue_cache,
                                       recently_used,
                                       cache,
                                       )


class LeastRecentlyUsed(unittest.TestCase):
    def test_shuffle_queue(self):
        self.setup_test_db()
        self.setup_test_cache()
        self.assertEqual(recently_used[0], 1)
        self.assertEqual(recently_used[1], 2)
        self.assertEqual(recently_used[2], 3)
        shuffle_queue(2)
        self.assertEqual(recently_used[0], 1)
        self.assertEqual(recently_used[1], 3)
        self.assertEqual(recently_used[2], 2)
        self.clear_test_cache()
        self.clear_test_db()

    def test_update_queue_cache_cache_not_full(self):
        self.assertEqual(len(recently_used), 0)
        update_queue_cache(5, 5)
        self.assertEqual(len(recently_used), 1)
        recently_used.clear()

    def test_update_queue_cache_cache_full(self):
        self.assertEqual(len(recently_used), 0)
        update_queue_cache(5, 5)
        self.assertEqual(len(recently_used), 1)
        update_queue_cache(6, 6)
        self.assertEqual(len(recently_used), 2)
        update_queue_cache(7, 7)
        self.assertEqual(len(recently_used), 3)
        update_queue_cache(8, 8)
        self.assertEqual(len(recently_used), 3)
        recently_used.clear()

    def test_get_value_from_cache(self):
        self.setup_test_db()
        self.setup_test_cache()

        get_value(1)
        self.assertEqual(recently_used[2], 1)
        recently_used.clear()
        cache.clear()

    def test_get_value_from_db(self):
        self.setup_test_db()
        self.assertEqual(cache.get(1), None)
        get_value(1)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(recently_used[0], 1)
        self.clear_test_cache()
        self.clear_test_db()

    def clear_test_cache(self):
        cache.clear()
        recently_used.clear()

    def setup_test_cache(self):
        cache.update({1: 1})
        cache.update({2: 2})
        cache.update({3: 3})
        recently_used.append(1)
        recently_used.append(2)
        recently_used.append(3)

    def setup_test_db(self):
        db.update({1: 1})
        db.update({2: 2})
        db.update({3: 3})
        db.update({4: 4})

    def clear_test_db(self):
        db.clear()
