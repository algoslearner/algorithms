'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

#TC : O(n)
#SC : O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #corner case: return false if string is all space
        if(s.isspace()):
            return True
        
        str = ''
        for c in s:
            if (c.isalpha() or c.isnumeric()):
                str += c
        
        str = str.lower()
        length = len(str)
        for i in range(0, length):
            if(str[i] != str[length-1-i]):
                       return False
        return True
