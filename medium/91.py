# Link to the problem: https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == "0":
            return 0

        n = len(s) + 1

        dp = [0] * n

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            if 1<=int(s[i-1])<= 9:
                dp[i] += dp[i-1]

            if 10<=int(s[i-2]+s[i-1])<= 26:
                dp[i] += dp[i-2]
            print(dp)

        return dp[-1]
