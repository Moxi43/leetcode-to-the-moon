// Link to the problem: https://leetcode.com/problems/combination-sum-iv/

func combinationSum4(nums []int, target int) int {
	dp := make([]int, target+1)
	dp[0] = 1
	summer := 0

	for i := min(nums); i < target+1; i++ {
		summer = 0
		for _, num := range nums {
			if i-num >= 0 {
				summer += dp[i-num]
			}
		}
		dp[i] = summer
	}
	return dp[len(dp)-1]
}

func min(x []int) int {
	out := x[0]
	for _, num := range x {
		if out > num {
			out = num
		}
	}
	return out
}