# solutions.py
from typing import List
class Solutions:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Function to find two indices such that nums[i] + nums[j] == target.
        """
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
        return [] 
    
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1: 'Solutions.ListNode', l2: 'Solutions.ListNode') -> 'Solutions.ListNode':
        """
        Function to add two numbers represented by linked lists.
        """
        dummy = self.ListNode()  # Dummy node to simplify result list construction
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get the current values, default to 0 if l1 or l2 is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = self.ListNode(total % 10)

            # Move to the next nodes
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the actual result, skipping the dummy node
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Implementation will go here
        raise NotImplementedError("subtract function not yet implemented")
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
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