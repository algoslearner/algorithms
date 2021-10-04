'''
Start of LinkedList Cycle 

142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
'''

# two pointers
# TC : O(n)
# SC : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        cycle_length = 0
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            # found cycle
            if slow == fast:
                cycle_length = self.calculateCycleLength(slow)
                break
        cycle_start = self.findStart(head, cycle_length)
        return cycle_start
    
    def calculateCycleLength(self, slow: ListNode) -> int:
        current = slow
        cycle_length = 0
        while True:
            current = current.next
            cycle_length += 1
            if current == slow:
                break
        return cycle_length
    
    def findStart(self, head: ListNode, cycle_length: int) -> ListNode:
        pointer1 = head
        pointer2 = head
        # move pointer2 to 'cycle_length' nodes ahead
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
        # increment both pointers until they meet at start of cycle
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1    
        
            
    
