# Link to the problem: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        if n == 1 and candidates[0] == target:
            res.append(candidates)
            return res
        
        def combineSum(curr_arr : List[int], curr_idx : int = 0) -> List[List[int]]:
            nonlocal res
            for i in range(curr_idx, n): 
                new_arr = curr_arr + [candidates[i]]
                new_sum = sum(new_arr)
                if new_sum == target:
                    res.append(new_arr)
                elif new_sum < target:
                    combineSum(new_arr, i)
                else: 
                    pass
                
            return res
        
        return combineSum([])