class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        
        for first, second in sorted(intervals):
            if not ans:
                ans.append([first, second])
            
            prev_high = ans[-1][1]
            if prev_high >= first:
                ans[-1][1] = max(prev_high, second)
                
            else:
                ans.append([first, second])
        
        return ans