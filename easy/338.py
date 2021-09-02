# Link to the problem: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = []
        for i in range(n+1):
            c = 0
            while i:
                c+=1 
                i &= i-1
            nums.append(c)
        return nums