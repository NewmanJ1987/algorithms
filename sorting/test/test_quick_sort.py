import unittest
from sorting.quick_sort import partition, quick_sort


class TestQuickSort(unittest.TestCase):
    def test_partion_odd_list(self):
        partitioned, index_to_split = partition([4, 3, 1, 8, 7])
        self.assertEqual(index_to_split, 2)
        self.assertEqual(partitioned, [3, 1, 4, 8, 7])

    def test_partition_even_list(self):
        partitioned, index_to_split = partition([4, 3, 1, 8])
        self.assertEqual(index_to_split, 2)
        self.assertEqual(partitioned, [3, 1, 4, 8])
