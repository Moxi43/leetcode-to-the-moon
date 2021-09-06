# Link to the problem: https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        nums.sort()
        return self.backtrack(0, nums, output, [])
    
    def backtrack(self, start, nums, output, temp):
        if start == len(nums):
            return 
            
        for i in range(len(nums)):
            temp.append(nums[i])
            if temp not in output:
                output.append(temp.copy())
                self.backtrack(start, nums[i + 1:], output, temp)
            temp.pop()
        return output
                
        
        