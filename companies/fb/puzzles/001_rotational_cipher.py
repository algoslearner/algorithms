'''
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
Output
Return the result of rotating input a number of times equal to rotationFactor.
Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?
Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
Need hints?

'''

# TC ; o(n)
# SC : O(1)

def rotationalCipher(input, rotation_factor):
  # Write your code here
  result = ""
  for c in input:
    if c.isdigit():
      newdigit = int(c) + rotation_factor
      result += str(newdigit)[-1]
    elif c.isalpha():
      if c.isupper():
        originalPosition = ord(c) - ord('A')
        newPosition = ((originalPosition + rotation_factor) % 26) + ord('A')
        result += chr(newPosition)
      elif c.islower():
        originalPosition = ord(c) - ord('a')
        newPosition = ((originalPosition + rotation_factor) % 26) + ord('a')
        result += chr(newPosition)
    else:
      result += c
  return result
