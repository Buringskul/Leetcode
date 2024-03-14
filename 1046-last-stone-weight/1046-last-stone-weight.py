class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        while len(stones) > 1:
            heavy1 = max(stones)
            stones.remove(heavy1)
            heavy2 = max(stones)
            stones.remove(heavy2)
            
            if heavy1 != heavy2:
                stones.append(abs(heavy1 - heavy2))
        
        if len(stones) == 0:
            return 0
        
        return stones[0]
            
            