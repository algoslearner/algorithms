'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# TC : O(n)
# SC : O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        parmap = {}
        parmap[')'] = '('
        parmap[']'] = '['
        parmap['}'] = '{'
        
        openpar = set()
        openpar.add('(')
        openpar.add('{')
        openpar.add('[')
        
        stack = []
        for c in s:
            if c in openpar:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    last_bracket = stack[-1]
                    if parmap[c] == last_bracket:
                        stack.pop()
                    else:
                        return False
        
        return stack == []
