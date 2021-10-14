'''
1275. Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

 

Example 1:


Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.
Example 2:


Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.
Example 3:


Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
Example 4:


Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
 

Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
'''

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols, diag, anti = [0]*3, [0]*3, 0, 0
        
        for turn, (x, y) in enumerate(moves):
            player = (turn % 2) * 2 - 1
            rows[x] += player
            cols[y] += player
            if x == y: diag += player
            if x + y == 2: anti += player
                
            if any(abs(cand) == 3 for cand in [rows[x], cols[y], diag, anti]):
                return "B" if player == 1 else "A"
            
        return "Draw" if len(moves) == 9 else "Pending"

'''
SOLUTION EXPLAINED

Not difficult problem, but in my opinion you need to code quite a lot for an easy problem. The idea is to keep number of X and O on each of vertical, horizontal and two diagonals. In fact we do not need to keep both of them, but do the following trick: we can add -1 to score if we meet X and +1 to score if we meet O. In this way game is finished if some score is equal to 3 or -3: if we have this numbers, it means, that we have full OOO of full XXX on the line.

So, we traverse moves one by one do the steps:

Calculate player, it will be either 1 or -1 depending on parity of turn.
Update rows[x], cols[y] and if needed diag and anti.
Check if given move will finish the game: it can happen if one of the values rows[x], cols[y], diag, anti becomes equal to 3 or -3.
In the end if we make 9 moves, we have Draw, in the opposite case it is Pending.
Complexity
If we have m moves, then we have O(m) time complexity. Space complexity is O(n), where here n = 3 is the size of our board.

'''
