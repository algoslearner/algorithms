'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
'''

# TC : O(n)
# SC : O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # load char frequency
        freq_map = {}
        for c in s:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1
        
        # check the string
        for i in range(len(s)):
            if s[i] in freq_map:
                if freq_map[s[i]] == 1:
                    return i
        return -1
