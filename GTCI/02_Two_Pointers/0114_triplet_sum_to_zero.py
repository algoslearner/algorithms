'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# two pointers
# SC : O(1)
# TC :  O(n2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # brute force : Time Limit Exceeded
        # TC : O(n2)
        # SC : O(1)
        '''
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        index = sorted ([nums[i], nums[j], nums[k]])
                        if index not in result:
                            result.append(index)
        return result
        '''
        
        # two pointers
        # TC : O(n2)
        # SC : O(1)
        result = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            target = 0 - nums[i]
            while left < right:
                if nums[left] + nums[right] == target:
                    index = sorted([nums[i], nums[left], nums[right]])
                    if index not in result:
                        result.append(index)
                    left += 1
                    right -= 1
                    # avoid duplicates
                    '''
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                    '''
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return result
                        
        
