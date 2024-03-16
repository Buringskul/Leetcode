class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        
        for i in sandwiches:
            if counter[i] == 0:
                break
            counter[i] -= 1
            
        return counter[0] + counter[1]
    