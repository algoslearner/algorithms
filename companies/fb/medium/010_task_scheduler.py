'''
621. Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
'''

'''
SOLUTION
Algorithm

The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.

Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.

Find the maximum frequency: f_max = max(frequencies).

Find the number of tasks which have the max frequency: n_max = frequencies.count(f_max).

If the number of slots to use is defined by the most frequent task, it's equal to (f_max - 1) * (n + 1) + n_max.

Otherwise, the number of slots to use is defined by the overall number of tasks: len(tasks).

Return the maximum of these two: max(len(tasks), (f_max - 1) * (n + 1) + n_max).
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        frequencies = [0]* 26
        for i in tasks:
            frequencies[ord(i) - ord('A')] += 1
            
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
    
        '''
        # max frequency
        freq_max = max(frequencies)
        
        # count the most frequent tasks
        n_max = frequencies.count(freq_max)
        
        return max(len(tasks), (freq_max - 1) * (n+1) + n_max)
        '''
        
        

 '''
 Complexity Analysis

Time Complexity: O(n), where n is a number of tasks to execute. This time is needed to iterate over the input array tasks and to compute the array frequencies. 
Array frequencies contains 26 elements, and hence all operations with it takes constant time.

Space Complexity: O(1), to keep the array frequencies of 26 elements.
