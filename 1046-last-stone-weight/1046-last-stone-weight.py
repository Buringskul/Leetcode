class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        q = [-stone for stone in stones]  
        heapq.heapify(q) 

        while len(q) > 1:
            first = -heapq.heappop(q) 
            second = -heapq.heappop(q) 

            if first != second:
                heapq.heappush(q, -abs(first - second))

        if not q: 
            return 0
        
        return -q[0] 
            
            