class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        
        while end >= start:
            mid = (start + end) // 2
            sqrdMid = mid * mid
            
            if sqrdMid == x:
                return mid
            
            elif sqrdMid > x:
                end = mid - 1
                
            else:
                start = mid + 1
                
        return end