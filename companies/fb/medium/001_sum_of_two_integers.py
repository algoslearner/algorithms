'''
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        # base case
        if b == 0: return a if a <= MAX else ~(a ^ mask)
        
        # calculation
        sum_withoutCarry = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        
        return self.getSum(sum_withoutCarry,carry)
 
'''
Prior Knowledge

You guys should check out the top posts to understand the general solution of:

def getSum(a, b):
	if b == 0: return a
	return getSum(a ^ b, (a & b) << 1)
But here's a quick summary:

Essentially, a ^ b add's binary numbers that do not require us to "carry" a "bit".
The (a & b) finds which bits need to be carried, and we simply bit shift to the left so the carried bit is in the right position.
By recursively calling getSum again, we will add the previous a^b result with the "carry" that needs to be accounted for to complete the add.
Python solution explanation

However, in python, integers can exceed 32 bits. This causes a problem for us! So to mitigate this, we have to:

Make sure our integers are strictly 32 bits
Juggle between 32 bit, 
two's complements.

First, lets talk about the mask variable. Notice that it is equal to 0b11111111111111111111111111111111. This is simply 32 bits of one's. This means any time the integer overflows to more than 32 bits, we do a & mask to set any bit greater than 32 to zero. This satifies our constraint #1 of making sure our intergers are strictly 32 bits.

Second, let's deal with the MAX variable. To understand the MAX variable, you must understand what is two's complement. Ultimately, MAX = 0b01111111111111111111111111111111 is the largest 32 bit integer that is "positve" under the "two's compelment" scheme. Thus, when we do if a <= MAX we are checking if a is positive. If a is greater than MAX, we have a "negative" number. However, since python can deal with integers greater than 32 bits, python assumes this negative integer is positive. Thus, ~(a ^ mask) allows us to juggle from the positive number to the negative complement, ensuring we return the correct answer.

class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0b11111111111111111111111111111111       
        MAX =  0b01111111111111111111111111111111
        
        if b == 0:
            return a if a <= MAX else ~(a ^ mask)
        
        return self.getSum(
            (a ^ b) & mask,
            ((a & b) << 1) & mask
        )
I hope this post has helped explain the python solution a tiny bit better!
'''
