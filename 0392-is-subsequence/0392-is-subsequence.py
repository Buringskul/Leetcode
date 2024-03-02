class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arrayIndex = 0
        seqIndex = 0

        while arrayIndex < len(t) and seqIndex < len(s):
            if t[arrayIndex] == s[seqIndex]:
                seqIndex += 1
            arrayIndex += 1
        return seqIndex == len(s)