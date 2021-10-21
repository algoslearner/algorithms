'''
1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
'''


# READ
# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/1065249/Python-3-solution-with-process-of-thinking-and-improvement

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        # python one-liner
        # return sorted(sorted(nums,reverse=1),key=nums.count)
        
        # using sort on freqmap
        '''
        freqmap = {}
        for i in range(len(nums)):
            freqmap[nums[i]] = freqmap.get(nums[i],0) + 1
        
        return sorted(nums,key=lambda x:(freqmap[x],-x))
        '''
        
        # learn to use Counter and sort on it
        '''
        r = Counter(nums).most_common()
        r.sort(key = lambda x: x[0], reverse=True)
        r.sort(key = lambda x: x[1])
        
        t = []
        for i in r:
            a, b = i
            t.extend([a]*b)
            
        return t
        '''
        
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))
