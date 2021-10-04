'''
581. Shortest Unsorted Continuous Subarray

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?
'''

# two pointers
# TC : O(n)
# SC : O(1)
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        # to find first unsorted number from left
        while left < len(nums) - 1 and nums[left] <= nums[left+1]:
            left += 1
        
        # corner case: array is sorted already
        if left == len(nums) - 1:
            return 0
        
        # to find the first unsorted number from right
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
            
        # find the max and min in this subarray
        subarray_max = float('-inf')
        subarray_min = float('inf')
        for k in range(left, right+1):
            subarray_max = max(subarray_max, nums[k])
            subarray_min = min(subarray_min, nums[k])
        
        # extend the subarray to left, to find if any number is bigger than subaary_min
        while left > 0 and nums[left-1] > subarray_min:
            left -= 1
        
        #extend subarray to right, if any number is lesser than subarray_max
        while right < len(nums) - 1 and nums[right+1] < subarray_max:
            right += 1
        
        return right - left + 1
