'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if(len(nums) <= 1):
            return False
        
        # TC : O(nlogn)
        # SC : O(1)
        '''
        nums.sort()
        for i in range(len(nums)):
            if(i != 0 and nums[i-1] == nums[i]):
                return True
        return False
        '''
    
        # TC : O(n)
        # SC : O(n)
        # return len(nums) != len(set(nums))
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
