# solutions.py
from typing import List
class Solutions:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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
        raise NotImplementedError("subtract function not yet implemented")
    
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def addTwoNumbers(self, l1: 'Solutions.ListNode', l2: 'Solutions.ListNode') -> 'Solutions.ListNode':
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
        raise NotImplementedError("subtract function not yet implemented")
    
    def lengthOfLongestSubstring(self, s: str) -> int:
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
        # Implementation will go here
        raise NotImplementedError("subtract function not yet implemented")
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Number 4.
        Given two sorted arrays nums1 and nums2 of size m and n respectively,
        return the median of the two sorted arrays. The overall run time
        complexity should be O(log (m+n)).

        Constraints:
        - nums1.length == m
        - nums2.length == n
        - 0 <= m <= 1000
        - 0 <= n <= 1000
        - 1 <= m + n <= 2000
        - -10^6 <= nums1[i], nums2[i] <= 10^6

        Example 1:
        Input: nums1 = [1, 3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.

        Example 2:
        Input: nums1 = [1, 2], nums2 = [3, 4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
        """
        # TODO: Implement the algorithm here
        raise NotImplementedError("Solution not yet implemented")
    
    def longestPalindrome(self, s: str) -> str:
        """
        This method returns the longest palindromic substring of a given string `s`.

        A palindrome is a string that reads the same forward and backward.

        Args:
        s: A string consisting of digits and English letters, where 1 <= len(s) <= 1000.

        Returns:
        A substring of `s` that is the longest palindrome.

        Constraints:
        - The input string's length is between 1 and 1000.
        - The string only contains digits and English letters (both uppercase and lowercase).
        
        Note: Raise NotImplementedError until the function is implemented.
        """
        raise NotImplementedError("Function longestPalindrome is not yet implemented.")