# Link to the problem: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for i in range(len(digits)):
            res += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(res+1)]
