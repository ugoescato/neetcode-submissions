class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        output = len(students)
        counter = Counter(students)
        
        for i in sandwiches:
            if counter[i] > 0:
                output -= 1
                counter[i] -= 1
            else:
                return output
        return output


        