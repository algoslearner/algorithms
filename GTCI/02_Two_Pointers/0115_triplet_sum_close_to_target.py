'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
'''

# TC : O(n2) + O(n log n)
# SC : O(n)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = math.inf
        closest_sum = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]
                target_diff = target - triplet_sum
                
                if abs(target_diff) < abs(min_diff):
                    min_diff = target_diff
                    closest_sum = triplet_sum
                
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1
        return closest_sum
                
                
