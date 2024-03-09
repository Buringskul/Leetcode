# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        bad = 0
        
        while end >= start:
            middle = (start + end) // 2
            if isBadVersion(middle):
                bad = middle
                end = middle - 1
            else:
                start = middle + 1
                
        return bad