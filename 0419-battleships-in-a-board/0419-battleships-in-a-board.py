class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if grid[i][j] == "X":
                grid[i][j] = "0"
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j + 1)
                dfs(grid, i, j - 1)
            else:
                return
        
        battleships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    dfs(board, i, j)
                    battleships += 1
        
        return battleships
                    