#Link to the problem: https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        def backtrack(total, index, memo):
            if (index, total) in memo:
                return memo[(index, total)]
            
            if total == target and index == len(nums):
                return 1
            
            elif index >= len(nums):
                return 0
            
            answer = 0
            
            answer += backtrack(total + nums[index], index+1, memo)
            
            answer += backtrack(total - nums[index], index+1, memo)
            
            memo[(index, total)] = answer
            
            return memo[(index, total)]
        
        return backtrack(0, 0, {})