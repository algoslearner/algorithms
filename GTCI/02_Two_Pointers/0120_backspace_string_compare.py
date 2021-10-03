'''
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".
Example 4:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        return self.check(s) == self.check(t)
        '''
        
        # two pointers
        # TC : O(n)
        # SC : O(1)
        index1 = len(s) - 1
        index2 = len(t) - 1
        while index1 >= 0 and index2 >= 0 :
            i1 = self.getNextValidIndex(s, index1)
            i2 = self.getNextValidIndex(t, index2)
            
            #print(i1)
            #print(i2)
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0 or i2 < 0:
                return False
            if s[i1] != t[i2]:
                return False
            index1 = i1 - 1
            index2 = i2 - 1
        return True
    
    def getNextValidIndex(self, str1: str, i: int) -> int:
        back = 0
        while i >= 0:
            if str1[i] == '#':
                back += 1
            elif back > 0:
                back -= 1
            else:
                break
            i -= 1
        print(i)
        return i
            
    
    # using stack
    # TC : O(n)
    # SC : O(1)
    '''
    def check(self, word: str) -> str:
        result = []
        for c in word:
            if c != '#':
                result.append(c)
            else:
                if result:
                    result.pop()
        return "".join(result)
    '''
