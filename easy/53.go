// Link to the problem: https://leetcode.com/problems/maximum-subarray/

func maxSubArray(nums []int) int {
	max_sum := nums[0]
	current_sum := nums[0]
	for i := 1; i < len(nums); i++ {
		current_sum = maxv(current_sum+nums[i], nums[i])
		max_sum = maxv(max_sum, current_sum)
	}
	return max_sum
}

func maxv(x int, y int) int {
	if x >= y {
		return x
	} else {
		return y
	}
}