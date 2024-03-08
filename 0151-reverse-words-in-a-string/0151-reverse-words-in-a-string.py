class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        answer = ""
        
        for i in reversed(words):
            answer += i + " "
        
        return answer[:-1]