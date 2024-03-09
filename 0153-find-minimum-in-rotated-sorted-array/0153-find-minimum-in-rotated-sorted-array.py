class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1
        if len(nums) == 1 or nums[0] < nums[end]:
            return nums[0]

        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[end] < nums[mid]:
                start = mid + 1
                
            elif nums[end] > nums[mid]:
                end = mid - 1
        