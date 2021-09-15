import "sort"

// Link to the problem: leetcode.com/problems/longest-increasing-subsequence

func lengthOfLIS(nums []int) int {
	var dp []int
	for _, num := range nums {
		i := BisectLeft(dp, num)
		if i == len(dp) {
			dp = append(dp, num)
		} else {
			dp[i] = num
		}
	}
	return len(dp)
}

func BisectLeft(a []int, v int) int {
	return bisectLeftRange(a, v, 0, len(a))
}

func bisectLeftRange(a []int, v int, lo, hi int) int {
	s := a[lo:hi]
	return sort.Search(len(s), func(i int) bool {
		return s[i] >= v
	})
}

