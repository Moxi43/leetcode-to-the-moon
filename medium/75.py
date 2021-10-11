# Link to the problem: https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 1, 2

        idx_r, idx_b = 0, len(nums)-1

        i = 0
        while i <= idx_b :

            if nums[i] == r:

                nums[idx_r], nums[i] = nums[i], nums[idx_r]

                idx_r += 1


            elif nums[i] == b:

                nums[idx_b], nums[i] = nums[i], nums[idx_b]

                idx_b -= 1

                i -= 1

            i += 1

