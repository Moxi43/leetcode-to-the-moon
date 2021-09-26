# Link to the problem: https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        dp = [[0] * n] * n

        n = len(s)
        res = 0

        dp = [[0 for i in range(n)] for j in range(n)]

        idx = 0
        while idx < n:
            dp[idx][idx] = 1
            idx += 1
            res += 1

        for col in range(1, len(s)):
            for row in range(col):
                if row == col - 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1

                elif dp[row + 1][col - 1] == 1 and s[col] == s[row]:
                    dp[row][col] = 1
                    res += 1
        return res
