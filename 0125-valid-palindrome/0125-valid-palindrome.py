class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s[::-1]:
            if i.isalnum():
                ans += i.lower()
        
        return ans == ans[::-1]