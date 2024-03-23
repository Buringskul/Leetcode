class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        
        while left < right:
            width = right - left
            
            if height[right] > height[left]:
                length = height[left]
                left += 1
                
            else:
                length = height[right]
                right -= 1
            
            area = max(area, length * width)
        
        return area