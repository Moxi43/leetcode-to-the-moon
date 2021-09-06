# Link to the problem: https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        for char in s:
            if char.isnumeric():
                result = [x+char for x in result]
            else:
                result = [x+char.lower() for x in result] + [x+char.upper() for x in result]
        
        return result
        
            