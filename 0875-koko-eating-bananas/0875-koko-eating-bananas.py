class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = ceil(sum(piles) / h) 
        right = sum(piles)
        
        while left < right:
            mid = (left + right) // 2
            time = 0
            
            for i in piles:
                time += ceil(i / mid)
                if time > h:
                    break
                    
            if time <= h:
                right = mid
            else:
                left = mid + 1
        
        return right