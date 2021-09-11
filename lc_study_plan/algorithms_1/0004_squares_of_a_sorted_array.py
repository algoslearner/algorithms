'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # brute force
        # TC : O(Nlogn)
        # SC : O(1)
        '''
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        
        nums.sort()
        return nums
        '''
        
        # using two pointers
        # TC : O(N)
        # SC : O(N) for output
        length = len(nums)
        
        start = 0
        end = length - 1
        output = [0] * length
        i = length - 1
        
        while(start <= end):
            if (nums[start]*nums[start] > nums[end]*nums[end]):
                output[i] = nums[start]*nums[start]
                start = start + 1
                i = i - 1
            else:
                output[i] = nums[end]*nums[end]
                end = end - 1
                i = i - 1
        return output
        
