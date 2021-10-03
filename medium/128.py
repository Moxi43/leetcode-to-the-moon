# Link to the problem: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak_counter = 0
        num_set = set(nums)

        for n in num_set:
            if n - 1 not in num_set:
                curr_n = n
                curr_streak = 1

                while curr_n + 1 in num_set:
                    curr_n += 1
                    curr_streak += 1

                streak_counter = max(streak_counter, curr_streak)

        return streak_counter
