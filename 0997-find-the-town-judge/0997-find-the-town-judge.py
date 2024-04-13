class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)  # Initialize trust count for each person
    
        # Iterate through each trust relationship and update trust count
        for a, b in trust:
            trust_count[a] -= 1  # Decrease trust count for person who trusts
            trust_count[b] += 1  # Increase trust count for person being trusted

        # Check for the person who is trusted by everyone else
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:  # If a person is trusted by everyone else
                return i  # Return the person's index as the judge

        return -1  # No judge found
