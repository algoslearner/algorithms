'''
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''

# using minHeap
# TC : O(log n + k log k)
# SC : O(k)

class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low)// 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        if low > 0: 
            return low - 1
        return low
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find index of number closest to 'x' with binary search
        index = self.binarySearch(arr, x)
        
        # range of k values
        low = index - k
        low = max(0, low)
        high = index + k
        high = min(high, len(arr)-1)
        
        minHeap = []
        for i in range(low,high+1):
            heapq.heappush(minHeap, (abs(x - arr[i]), arr[i]))
        
        # add k closest values to output array
        result = []
        for _ in range(k):
            result.append(heappop(minHeap)[1])
        result.sort()
        return result
