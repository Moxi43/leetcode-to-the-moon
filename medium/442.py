# Link to the problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = (nums[i]%len(nums))-1 
            nums[index]+=len(nums)
        output = []
        for i,v in enumerate(nums):
            if v>2*len(nums):
                output.append(i+1)
        return output
