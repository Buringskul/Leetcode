class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        answer = 0
        max_length = 0
        max_area = [0] * len(height) 
        
        for i in range(len(height)):
            if height[i] != 0:
                left = i
                break
        
        for i in range(len(height) - 1, -1, -1):
            if height[i] != 0:
                right = i
                break

        while left < right:
            if height[left] >= height[right]:
                length = height[right]
                right -= 1
            else:
                length = height[left]
                left += 1

            if length > max_length:
                for i in range(left, right + 1):
                    max_area[i] = length
            max_length = max(max_length, length)
        
        for i in range(len(height) - 1):
            if height[i] >= max_area[i]:
                max_area[i] = 0
            else:
                max_area[i] = max_area[i] - height[i]
                
            answer += max_area[i]
             
        return answer
        

    