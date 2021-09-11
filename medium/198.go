// Link to the problem: https://leetcode.com/problems/house-robber/

func rob(nums []int) int {
	rob, notRob := nums[0], 0
	n := len(nums)
	for i := 1; i < n; i++ {
		oldRob := rob
		rob = notRob + nums[i]
		notRob = max(oldRob, notRob)
	}
	return max(rob, notRob)
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}
