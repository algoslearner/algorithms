'''
408. Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
'''

# TC : O(n)
# SC : O(1)

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = 0
        count = 0
        
        # index for abbr string is i
        i = 0
        while i < len(abbr):
            ch = abbr[i]
            if abbr[i].isdigit():
                
                # check for leading zero
                if abbr[i] == '0': return False
                
                # get entire number in abbr to count variable
                count = 0
                while i < len(abbr) and abbr[i].isdigit():
                    count = count * 10 + int(abbr[i])
                    i += 1
                index += count
                
                # Ensure that the abbreviation number isn't longer than the entire remaining portion of word
                if index > len(word): return False
                
            elif abbr[i].isalpha():
                if index < len(word) and word[index] != ch: return False
                index += 1
                i += 1

                
        return i == len(abbr) and index == len(word)
