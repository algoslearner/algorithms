'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # brute force : TLE
        # TC : O(n4)
        # SC : O(1)
        '''
        result = []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    for p in range(k+1,len(nums)):
                        if(nums[i] + nums[j] + nums[k] + nums[p] == target):
                            quad = sorted([nums[i],nums[j],nums[k],nums[p]])
                            if quad not in result:
                                result.append(quad)
        return result
        '''
        
        # two pointers
        # TC : O(n3)
        # SC : O(1)
        result = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                self.searchPairs(nums, target, i, j, result)
        return result
    
    def searchPairs(self, nums: List[int], target: int, i1: int, j1: int, result: List[List[int]]):
        left = j1 + 1
        right = len(nums) - 1
        while left < right:
            quad_sum = nums[i1] + nums[j1] + nums[left] + nums[right]
            if quad_sum == target:
                result.append([nums[i1], nums[j1], nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif quad_sum < target:
                left += 1
            else:
                right -= 1
            
        
    
    
        
