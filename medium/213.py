# Link to the problem: https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums: List[int], l: int, r: int) -> int:
            if len(nums) == 2:
                return max(nums[l], nums[r])
            
            val1 = nums[l]
            val2 = 0
            res = 0
            
            for i in range(l+1, r+1):
                res = max(val1, val2)
                val1 = val2 + nums[i]
                val2 = res
            return max(val1, val2)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(robRange(nums, 0, len(nums)-2), robRange(nums, 1, len(nums)-1))