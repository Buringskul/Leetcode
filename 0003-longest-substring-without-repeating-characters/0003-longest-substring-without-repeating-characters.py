class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        subString = []
        maxLength = 0
        
        for char in s:
            if char in subString:
                subString = subString[subString.index(char)+1:]

            subString.append(char)
            maxLength = max(maxLength, len(subString))
        
        return maxLength;