"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/permutation-in-string/description
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        pattern_count = Counter(s1)
        window_count = Counter()
        left = 0
        for right in range(len(s2)):
            window_count[s2[right]] += 1
            if right - left + 1 == len(s1):
                if window_count == pattern_count:
                    return True
                window_count[s2[left]] -= 1
                left += 1
        return False


answer = Solution()
print(answer.checkInclusion("ab", "eidbaooo"))
print(answer.checkInclusion("ab", "eidboaoo"))
