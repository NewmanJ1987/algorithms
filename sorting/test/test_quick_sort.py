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

    def test_quick_sort_even_list(self):
        in_order = quick_sort([4, 3, 1, 8])
        self.assertEqual([1, 3, 4, 8], in_order)

    def test_quick_sort_odd_list(self):
        in_order = quick_sort([4, 3, 1, 8, 7])
        self.assertEqual([1, 3, 4, 7, 8], in_order)

    def test_quick_sort_empty_list(self):
        in_order = quick_sort([])
        self.assertEqual([], in_order)

    def test_quick_sort_one_element_list(self):
        in_order = quick_sort([4])
        self.assertEqual([4], in_order)
