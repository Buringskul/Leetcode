class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        occur = set()
        
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        for value in hashmap.values():
            if value in occur:
                return False
            else:
                occur.add(value)
                
        return True;