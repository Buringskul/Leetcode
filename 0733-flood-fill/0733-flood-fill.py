class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(grid, i, j, change, color):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if grid[i][j] == change:
                grid[i][j] = color
                dfs(grid, i + 1, j, change, color)
                dfs(grid, i - 1, j, change, color)
                dfs(grid, i, j + 1, change, color)
                dfs(grid, i, j - 1, change, color)
            else:
                return
            
        if image[sr][sc] == color:
            return image
        
        dfs(image, sr, sc, image[sr][sc], color)
        return image