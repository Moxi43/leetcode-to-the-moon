// Link to the problem: https://leetcode.com/problems/contains-duplicate/

func containsDuplicate(nums []int) bool {
	m := make(map[int]bool, len(nums))

	for _, i := range nums {
		if _, found := m[i]; found {
			return true
		}
		m[i] = true
	}
	return false
}
