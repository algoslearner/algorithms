'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

# TC : O(N)
# SC : O(k)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # store pattern in char-freq hashmap
        freq = {}
        for c in s1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        # iterate through big word, s2
        start = 0
        charmatch = 0
        for end in range(len(s2)):
            rightchar = s2[end]
            if rightchar in freq:
                freq[rightchar] -= 1
                if freq[rightchar] == 0: 
                    charmatch += 1
            
            # found permutaion of given pattern
            if charmatch == len(freq):
                return True
            
            # slide window: keep window size as pattern length
            if end >= len(s1) - 1:
                leftchar = s2[start]
                if leftchar in freq:
                    if freq[leftchar] == 0: charmatch -= 1
                    freq[leftchar] += 1
                start += 1
        
        return False
