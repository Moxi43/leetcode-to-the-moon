// Link to the problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

func findDisappearedNumbers(nums []int) []int {
	missed := make([]int, len(nums)+1)
	var res []int

	for _, i := range nums {
		missed[i] = i
	}

	for i := 1; i < len(missed); i++ {
		if missed[i] == 0 {
			res = append(res, i)
		}
	}
	return res
}