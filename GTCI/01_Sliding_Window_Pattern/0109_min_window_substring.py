'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

# TC : O(M+N)
# SC : O(M)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # store pattern string to hashmap
        freq = {}
        for c in t:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        # parse the bigger string
        start = 0
        charmatch = 0
        substring_start = ""
        min_length = len(s) + 1
        for end in range(len(s)):
            rightchar = s[end]
            if rightchar in freq:
                freq[rightchar] -= 1
                # count each charmatch
                if freq[rightchar] >= 0: charmatch += 1
            
            while charmatch == len(t):
                if min_length > end - start + 1:
                    min_length = end - start + 1
                    substring_start = start
                    
                leftchar = s[start]
                if leftchar in freq:
                    if freq[leftchar] == 0: charmatch -= 1
                    freq[leftchar] += 1
                start += 1
        
        # return substring
        if min_length > len(s):
            return ""
        
        return s[substring_start:substring_start+min_length]
        
