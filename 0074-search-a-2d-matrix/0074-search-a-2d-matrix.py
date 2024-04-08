class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        start = 0
        end = rows * cols - 1
        
        while start <= end:
            middle = start + (end - start) // 2
            element = matrix[middle // cols][middle % cols]
            
            if element == target:
                return True
            
            elif element < target:
                start = middle + 1
            
            else:
                end = middle - 1
                
        return False