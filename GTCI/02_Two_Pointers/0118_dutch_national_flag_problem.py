'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        
        # TC : O(n)
        # SC : O(1)
        '''
        count_red = 0
        count_white = 0
        count_blue = 0
        for n in nums:
            if n == 0:
                count_red += 1
            elif n == 1:
                count_white += 1
            elif n == 2:
                count_blue += 1
        
        # recreate array with new index
        i = 0
        while count_red > 0 and i < len(nums):
            nums[i] = 0
            i += 1
            count_red -= 1
        while count_white > 0 and i < len(nums):
            nums[i] = 1
            i += 1
            count_white -= 1
        while count_blue > 0 and i < len(nums):
            nums[i] = 2
            i += 1
            count_blue -= 1
        '''
        
        # dutch-flag-sort
        # TC : O(n)
        # SC : O(1)
        low = 0
        high = len(nums) - 1
        i = 0
        while i <= high:
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                i += 1
                low += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1
     
