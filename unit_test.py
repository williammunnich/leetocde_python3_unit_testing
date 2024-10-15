import unittest
from solutions import Solutions
from typing import List
from math_operations import add, subtract, multiply, divide

class Test_MathOperations(unittest.TestCase):

    def test_add(self):
        try:
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-1, 1), 0)
            self.assertEqual(add(-1, -1), -2)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised
    
    def test_subtract(self):
        try:
            self.assertEqual(subtract(5, 3), 2)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised
    
    def test_multiply(self):
        try:
            self.assertEqual(multiply(2, 3), 6)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised

    def test_divide(self):
        try:
            self.assertEqual(divide(10, 2), 5)
            self.assertEqual(divide(-10, 5), -2)
            self.assertEqual(divide(0, 1), 0)
            with self.assertRaises(Exception):
                divide(10, 0)  # This should raise an error for division by zero
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised

class test_prob1(unittest.TestCase):
    """
    Problem 1: Two Sum
    
    Problem Description:
    Given an array of integers `nums` and an integer `target`, return the indices of the two numbers 
    such that they add up to `target`. You may assume that there is exactly one solution, and 
    you may not use the same element twice. The indices can be returned in any order.

    Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]
    Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].

    Constraints:
    - The length of `nums` is between 2 and 10^4.
    - Each integer in `nums` is between -10^9 and 10^9.
    - There is exactly one valid solution for each input.
    """
    def setUp(self):
        self.solution = Solutions()

    def test_twoSum_example1(self):
        try:
            nums = [2, 7, 11, 15]
            target = 9
            expected_output = [0, 1]
            result = self.solution.twoSum(nums, target)
            self.assertEqual(result, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))  # Skip test if NotImplementedError is raised

    def test_twoSum_example2(self):
        try:
            nums = [3, 2, 4]
            target = 6
            expected_output = [1, 2]
            result = self.solution.twoSum(nums, target)
            self.assertEqual(result, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))

    def test_twoSum_example3(self):
        try:
            nums = [3, 3]
            target = 6
            expected_output = [0, 1]
            result = self.solution.twoSum(nums, target)
            self.assertEqual(result, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))

    def test_twoSum_large_input(self):
        try:
            nums = [i for i in range(1, 10001)]
            target = 19999
            expected_output = [9998, 9999]  # 9999 + 10000 == 19999
            result = self.solution.twoSum(nums, target)
            self.assertEqual(result, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))


class test_prob2(unittest.TestCase):
    """
    Problem 2: Add Two Numbers
    
    Problem Description:
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    
    Example 1:
    Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    Output: [7, 0, 8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    Output: [8, 9, 9, 9, 0, 0, 0, 1]
    
    Constraints:
    - The number of nodes in each linked list is between 1 and 100.
    - Each node contains an integer between 0 and 9.
    """
    def setUp(self):
        self.solution = Solutions()

    def list_to_linkedlist(self, numbers):
        """Helper function to convert a list to a linked list."""
        dummy = self.solution.ListNode()  # Using ListNode inside Solution
        current = dummy
        for num in numbers:
            current.next = self.solution.ListNode(num)
            current = current.next
        return dummy.next

    def linkedlist_to_list(self, node):
        """Helper function to convert a linked list to a list."""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_addTwoNumbers_example1(self):
        try:
            l1 = self.list_to_linkedlist([2, 4, 3])
            l2 = self.list_to_linkedlist([5, 6, 4])
            expected_output = [7, 0, 8]
            result = self.solution.addTwoNumbers(l1, l2)
            result_list = self.linkedlist_to_list(result)
            self.assertEqual(result_list, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))

    def test_addTwoNumbers_example2(self):
        try:
            l1 = self.list_to_linkedlist([0])
            l2 = self.list_to_linkedlist([0])
            expected_output = [0]
            result = self.solution.addTwoNumbers(l1, l2)
            result_list = self.linkedlist_to_list(result)
            self.assertEqual(result_list, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))

    def test_addTwoNumbers_example3(self):
        try:
            l1 = self.list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
            l2 = self.list_to_linkedlist([9, 9, 9, 9])
            expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
            result = self.solution.addTwoNumbers(l1, l2)
            result_list = self.linkedlist_to_list(result)
            self.assertEqual(result_list, expected_output)
        except NotImplementedError as e:
            self.skipTest(str(e))

    """
    Problem 2: Add Two Numbers
    
    Problem Description:
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
    
    Example 1:
    Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
    Output: [7, 0, 8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
    Output: [8, 9, 9, 9, 0, 0, 0, 1]
    
    Constraints:
    - The number of nodes in each linked list is between 1 and 100.
    - Each node contains an integer between 0 and 9.
    """
    def setUp(self):
        self.solution = Solutions()

    def list_to_linkedlist(self, numbers):
        """Helper function to convert a list to a linked list."""
        dummy = self.solution.ListNode()  # Using ListNode inside Solution
        current = dummy
        for num in numbers:
            current.next = self.solution.ListNode(num)
            current = current.next
        return dummy.next

    def linkedlist_to_list(self, node):
        """Helper function to convert a linked list to a list."""
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_addTwoNumbers_example1(self):
        l1 = self.list_to_linkedlist([2, 4, 3])
        l2 = self.list_to_linkedlist([5, 6, 4])
        expected_output = [7, 0, 8]
        
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = self.linkedlist_to_list(result)
        
        self.assertEqual(result_list, expected_output)

    def test_addTwoNumbers_example2(self):
        l1 = self.list_to_linkedlist([0])
        l2 = self.list_to_linkedlist([0])
        expected_output = [0]
        
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = self.linkedlist_to_list(result)
        
        self.assertEqual(result_list, expected_output)

    def test_addTwoNumbers_example3(self):
        l1 = self.list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linkedlist([9, 9, 9, 9])
        expected_output = [8, 9, 9, 9, 0, 0, 0, 1]
        
        result = self.solution.addTwoNumbers(l1, l2)
        result_list = self.linkedlist_to_list(result)
        
        self.assertEqual(result_list, expected_output)
        
        
class test_prob3(unittest.TestCase):
    """
    3. Longest Substring Without Repeating Characters
    Medium

    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:
    - 0 <= s.length <= 5 * 10^4
    - s consists of English letters, digits, symbols and spaces.
    """

    def setUp(self):
        self.solution = Solutions()

    def test_example_1(self):
        s = "abcabcbb"
        expected = 3
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")

    def test_example_2(self):
        s = "bbbbb"
        expected = 1
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")

    def test_example_3(self):
        s = "pwwkew"
        expected = 3
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")

    def test_empty_string(self):
        s = ""
        expected = 0
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")

    def test_single_character_string(self):
        s = "a"
        expected = 1
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")

    def test_all_unique_characters(self):
        s = "abcdef"
        expected = 6
        try:
            self.assertEqual(self.solution.lengthOfLongestSubstring(s), expected)
        except NotImplementedError:
            self.skipTest("Solution not implemented")
            
            
# Unit test class for the solution
class test_prob4(unittest.TestCase):
    def setUp(self):
        self.solution = Solutions()

    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected_output = 2.0
        try:
            self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_output)
        except NotImplementedError as e:
            self.skipTest(f"Test skipped: {e}")

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected_output = 2.5
        try:
            self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_output)
        except NotImplementedError as e:
            self.skipTest(f"Test skipped: {e}")

    # Additional test cases
    def test_single_element(self):
        nums1 = []
        nums2 = [1]
        expected_output = 1.0
        try:
            self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_output)
        except NotImplementedError as e:
            self.skipTest(f"Test skipped: {e}")

    def test_empty_nums1(self):
        nums1 = []
        nums2 = [2, 3]
        expected_output = 2.5
        try:
            self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_output)
        except NotImplementedError as e:
            self.skipTest(f"Test skipped: {e}")

    def test_negative_numbers(self):
        nums1 = [-5, -3, -1]
        nums2 = [-2, 0, 2]
        expected_output = -1.5
        try:
            self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected_output)
        except NotImplementedError as e:
            self.skipTest(f"Test skipped: {e}")
        
if __name__ == '__main__':
    unittest.main()
