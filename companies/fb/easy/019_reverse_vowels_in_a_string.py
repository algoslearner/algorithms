'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

# TC : O(n)
# SC : O(1)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        
        # edge case
        if s.isspace(): return s
        
        start = 0
        end = len(s) - 1
        result = ['']* len(s)
        while start <= end:
            while start < len(s) and s[start] not in vowels:
                result[start] = s[start]
                start += 1
            while end >= 0 and s[end] not in vowels:
                result[end] = s[end]
                end -= 1
            
            # validate exit condition
            if start > end:
                break
                
            # reverse start and end vowels
            result[start] = s[end]
            result[end] = s[start]
            start += 1
            end -= 1
            
        return "".join(result)
