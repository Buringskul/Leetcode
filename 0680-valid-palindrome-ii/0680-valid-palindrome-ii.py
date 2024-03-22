class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(skip, left, right):
            if skip > 1:
                return False

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return isPalindrome(skip+1, left+1, right) or isPalindrome(skip+1, left, right-1)
            
            return True
                
        return isPalindrome(0, 0, len(s)-1)
    
    