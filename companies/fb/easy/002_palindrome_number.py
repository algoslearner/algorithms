'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

# TC : O(n)
# SC : O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # edge case: negative numbers
        if x < 0: return False
        
        # convert into string
        '''
        s = str(x)
        for i in range(0, int(len(s)/2)):
            if s[i] != s[-1-i]:
                return False
        return True
        '''
        
        # reverted number
         
        reverse = 0
        givennum = x
        while givennum >= 1:
            lastdigit = int(givennum % 10)
            reverse = reverse * 10 + lastdigit
            givennum /= 10
        return x == reverse
        
