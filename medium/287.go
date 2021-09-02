// Link to the problem: https://leetcode.com/problems/find-the-duplicate-number/

func findDuplicate(nums []int) int {
	slow := nums[0]
	fast := nums[0]

	for {
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast {
			break
		}
	}

	slow = nums[0]
	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}
	return fast
}