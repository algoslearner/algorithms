'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == None or len(s) == 0: 
            return 0
        
        length = 0
        hashmap = {}
        windowStart = 0
        for windowEnd in range(len(s)):
            c = s[windowEnd]
            if c in hashmap:
                if hashmap.get(c) >= windowStart:
                    windowStart = hashmap.get(c) + 1
            length = max(length, windowEnd - windowStart+1)
            hashmap[c] = windowEnd
        return length
