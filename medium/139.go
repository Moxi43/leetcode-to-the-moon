import "fmt"

// Link to the problem: https://leetcode.com/problems/word-break/

func wordBreak(s string, wordDict []string) bool {
	dp := make([]bool, len(s)+1)
	dp[0] = true

	for i := range s {
		if !dp[i] {
			continue
		}

		for _, word := range wordDict {

			if i+len(word) > len(s) {
				continue
			}

			if s[i:i+len(word)] == word {
				dp[i+len(word)] = true
			}
		}
	}
	fmt.Println(dp)
	return dp[len(s)]
}
