'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

# TC : O(N)
# SC : O(1)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0:
            num_a = int(a[i]) if i >= 0 else 0
            num_b = int(b[j]) if j >= 0 else 0
            
            i -= 1
            j -= 1
            nums_sum = num_a + num_b + carry
            result.append(str(nums_sum % 2))
            carry = nums_sum // 2
        
        if carry:
            result.append(str(carry))
        return "".join(list(reversed(result)))
