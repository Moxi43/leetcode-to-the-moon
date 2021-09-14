# Link to the problem: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_current = max_global = min_current = nums[0]
        for i in range(1, len(nums)):
            min_current_local = min(max_current*nums[i], min_current*nums[i], nums[i])
            max_current_local = max(max_current*nums[i], min_current*nums[i], nums[i])
            max_global = max(max_current_local, max_global)
            max_current = max_current_local
            min_current = min_current_local
        
        return max_global
            
            