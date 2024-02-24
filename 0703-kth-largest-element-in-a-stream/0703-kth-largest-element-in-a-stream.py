class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.numbers = nums
        heapq.heapify(self.numbers)
        while len(self.numbers) > k:
            heapq.heappop(self.numbers)
    
    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, val)
        if len(self.numbers) > self.k:
            heapq.heappop(self.numbers)
        return self.numbers[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)