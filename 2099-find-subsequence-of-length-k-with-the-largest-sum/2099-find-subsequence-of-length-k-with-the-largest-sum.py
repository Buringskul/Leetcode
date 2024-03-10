class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k
        
        while n != 0:
            nums.remove(min(nums))
            n -= 1
            
        return nums