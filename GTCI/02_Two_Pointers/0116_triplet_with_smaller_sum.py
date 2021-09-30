'''
259. 3Sum Smaller

Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
 

Constraints:

n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100
'''

# TC : O(n2) + O(n logn)
# SC : O(n)

# Sorting takes TC : O(nlogn) and SC: O(n)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            target_sum = target - nums[i]
            while left < right:
                if nums[left] + nums[right] < target_sum:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count        
