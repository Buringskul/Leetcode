class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            if height[left] > height[right]:
                length = height[right]
                right -= 1
            else:
                length = height[left]
                left += 1
            
            area = max(area, length * width)
        
        return area
            