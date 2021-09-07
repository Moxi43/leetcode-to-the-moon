# Link to the problem: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        ans = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            sub_prop = self.permute(nums[1:])
            for sub_ans in sub_prop:
                ans.append([nums[0]] + sub_ans)
            nums[0], nums[i] = nums[i], nums[0]
        
        return ans 