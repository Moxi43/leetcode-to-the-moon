// Link to the problem: https://leetcode.com/problems/missing-number/

func missingNumber(nums []int) int {
	sum := 0
	s := len(nums)
	for _, i := range nums {
		sum += i
	}

	return s*(s+1)/2 - sum
}