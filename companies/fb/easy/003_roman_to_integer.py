'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

# TC : O(1), finite input size
# SC : O(1), finite input size

class Solution:
    def romanToInt(self, s: str) -> int:
        # add values
        roman_map = {}
        roman_map["I"] = 1
        roman_map["V"] = 5
        roman_map["X"] = 10
        roman_map["L"] = 50
        roman_map["C"] = 100
        roman_map["D"] = 500
        roman_map["M"] = 1000
        roman_map["IV"] = 4
        roman_map["IX"] = 9
        roman_map["XL"] = 40
        roman_map["XC"] = 90
        roman_map["CD"] = 400
        roman_map["CM"] = 900
        
        # check the input string
        num = 0
        i = 0
        while i < len(s):
            if (s[i] == "C" or s[i] == "X" or s[i] == "I") and i+1 < len(s):
                key = s[i]
                key += s[i+1]
                if key in roman_map:
                    num += roman_map[key]
                    i += 1
                else:
                    num += roman_map[s[i]]
            else:
                num += roman_map[s[i]]
            i += 1
        return num
