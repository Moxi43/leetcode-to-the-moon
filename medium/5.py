#Link to the problem: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            #odd
            local_palindrome = self.indexer(s, i, i)
            if len(local_palindrome) > len(max_palindrome):
                max_palindrome = local_palindrome
            #even
            local_palindrome = self.indexer(s, i, i+1)
            if len(local_palindrome) > len(max_palindrome):
                max_palindrome = local_palindrome
                
        return max_palindrome
            
            
    def indexer(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left+1:right]
        