'''
319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1
 

Constraints:

0 <= n <= 109
'''

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
        # return int(n**(1/2))
'''
 There is a pattern for it
for 1th bulb : 1
2nd : 1 0
3rd : 1 0 0
4th : 1 0 0 1
5th : 1 0 0 1 0
6th : 1 0 0 1 0 0
7th : 1 0 0 1 0 0 0
8th : 1 0 0 1 0 0 0 0
9th : 1 0 0 1 0 0 0 0 1

Meaning the I-th bulb that is on only on when its on I**2 turn, for example if you want 2 bulb on then you will have to go to 4th round, 3 bulb on -> 9th round.
so for (n-th round) you can get at most floor(square_root(n)) bulb.
'''
