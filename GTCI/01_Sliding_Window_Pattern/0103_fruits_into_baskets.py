'''
904. Fruit Into Baskets

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
Example 4:

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can pick from trees [1,2,1,1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
'''

# TC : O(N)
# SC : O(N)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        freq = {}
        max_count = 0
        
        for end in range(len(fruits)):
            right_type = fruits[end]
            if right_type in freq:
                freq[right_type] += 1
            else:
                freq[right_type] = 1
            
            # slide window if there are two distict fruits
            while len(freq) > 2:
                left_type = fruits[start]
                freq[left_type] -= 1
                if freq[left_type] == 0:
                    del freq[left_type]
                start += 1
            
            # recalculate max_count of fruits picked
            window_size = end - start + 1
            max_count = max(max_count, window_size)
        return max_count
