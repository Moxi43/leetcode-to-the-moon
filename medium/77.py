# Link to the problem: https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(index = 1, combination = []):
            if len(combination) == k:
                res.append(combination.copy())
                return
            
            for i in range(index, n+1):
                combination.append(i)
                backtrack(i+1, combination)
                combination.pop()
        backtrack()
        return res