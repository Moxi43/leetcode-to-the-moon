import "sort"

// Link to the problem: https://leetcode.com/problems/squares-of-a-sorted-array/

func sortedSquares(nums []int) []int {
	slow := 0
	fast := len(nums) - 1

	for slow <= fast {
		if slow < fast {
			nums[slow] = nums[slow] * nums[slow]
			nums[fast] = nums[fast] * nums[fast]
			slow += 1
			fast -= 1
		} else {
			nums[slow] = nums[slow] * nums[slow]
			break
		}
	}
	sort.Ints(nums)
	return nums
}