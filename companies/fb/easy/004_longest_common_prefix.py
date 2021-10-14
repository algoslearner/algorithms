'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''

# TC : O(n)
# SC : O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        
        prefix = ""
        firstword = strs[0]
        mismatch = 0
        for i in range(len(firstword)):
            for s in strs:
                if i >= len(s) or firstword[i] != s[i]:
                    mismatch = 1
                    break
            if mismatch == 0:
                prefix += firstword[i]
            else:
                break
        return prefix
