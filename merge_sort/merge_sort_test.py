import unittest
from merge_sort import MergeSort 

class MergeSortTest(unittest.TestCase):
    
    def test_merge_sort(self):
        print("Inside test_merge_sort")
        arr = [6,5,3,1,8,7,2,4,4]
        ms = MergeSort()
        sorted_arr = ms.merge_sort(arr)
        self.assertEqual([1,2,3,4,4,5,6,7,8], sorted_arr)
        
    def test_merge_sort_empty(self):
        print("Inside test_merge_sort_empty")
        arr = []
        ms = MergeSort()
        sorted_arr = ms.merge_sort(arr)
        self.assertEqual([], sorted_arr)
        
    def test_merge_sort_two(self):
        print("Inside test_merge_sort_two")
        arr = [6,3]
        ms = MergeSort()
        sorted_arr = ms.merge_sort(arr)
        self.assertEqual([3,6], sorted_arr)


if __name__ == '__main__':
    unittest.main()