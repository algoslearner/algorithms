'''
1481. Least Number of Unique Integers after K Removals

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        counter = Counter(arr)
        min_heap = []
        for key, val in counter.items():
            heapq.heappush(min_heap, val)
        ans = len(counter)
        while k > 0:
            cur_freq = heapq.heappop(min_heap)
            if cur_freq <= k:
                k -= cur_freq
                ans -= 1
            else:
                break
        return ans
    
        '''
        
        if len(arr) <= k:
            return 0
        
        # count freq of each number
        freqmap = {}
        for i in range(len(arr)):
            freqmap[arr[i]] = freqmap.get(arr[i],0) + 1
        
        # insert all numbers with freq greater than one, to min heap
        minHeap = []
        distinct = 0
        for c, freq in freqmap.items():
            if freq == 1:
                distinct += 1
            else:
                heapq.heappush(minHeap,(freq,c))
        
        # remove the least frequent numbers from minHeap
        # to make an element distinct, we need to remove all of its occurrences except one
        while k > 0 and minHeap:
            freq, c = heapq.heappop(minHeap)
            freq = freq - 1
            k -= freq
            if k >= 0:
                distinct += 1
        
        # if k > 0, this means we have to remove some distinct numbers
        if k > 0:
            distinct -= k
        
        return distinct
        '''
        
            
