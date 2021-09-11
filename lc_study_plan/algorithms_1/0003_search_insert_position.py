'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

# TC : O(log n)
# SC : O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums) == 0):
            return -1
        
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end - start) // 2
            if(nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                start = mid + 1
            else:
                end = mid - 1
        return start
