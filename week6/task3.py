"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        total_count = 0
        left = 0
        char_count = {"a": 0, "b": 0, "c": 0}
        for right in range(len(s)):
            char_count[s[right]] += 1
            while all(char_count[char] > 0 for char in "abc"):
                total_count += len(s) - right
                char_count[s[left]] -= 1
                left += 1
        return total_count


answer = Solution()
print(answer.numberOfSubstrings("abcabc"))
print(answer.numberOfSubstrings("aaacb"))
