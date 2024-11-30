"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/find-all-anagrams-in-a-string/description
"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        p_count = Counter(p)
        window_count = Counter()
        left = 0
        index_list = []
        for right in range(len(s)):
            window_count[s[right]] += 1
            if right - left + 1 == len(p):
                if window_count == p_count:
                    index_list.append(left)
                window_count[s[left]] -= 1
                left += 1
        return index_list


answer = Solution()
print(answer.findAnagrams("cbaebabacd", "abc"))
print(answer.findAnagrams("abab", "ab"))
print(answer.findAnagrams("baa", "aa"))
print(answer.findAnagrams("abaacbabc", "abc"))
