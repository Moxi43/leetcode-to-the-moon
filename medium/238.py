# Link to the problem: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = 1
        for num in nums:
            k*= num
        
        res = []
        for i in range(len(nums)):
            if nums[i] is not 0:
                res.append(k//nums[i])
            else:
                res.append(self.prod(nums, i))
        return res
        
    def prod(self, nums, t):
        p=1
        for i in range(len(nums)):
            if i!=t:
                p*=nums[i]
        
        return p