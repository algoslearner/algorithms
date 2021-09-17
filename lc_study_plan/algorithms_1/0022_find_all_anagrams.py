'''
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

# TC : O(N)
# SC: O(1)
# sliding window

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return
        p_count = [0] * 26
        s_count = [0] * 26
        
        for i in p:
            p_count[ord(i) - ord('a')] += 1
        
        output = []
        lp = len(p)
        ls = len(s)
        # sliding window on string s
        for i in range(ls):
            
            # add one letter to right of window
            s_count[ord(s[i]) - ord('a')] += 1
            
            #remove one letter from left of window
            if (i >= len(p)):
                s_count[ord(s[i - lp]) - ord('a')] -= 1
            
            if p_count == s_count:
                output.append(i - lp + 1)
        
        return output
