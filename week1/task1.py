"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, stroka: str) -> int:
        cnt_sub = 0
        max_sub = 0
        start_index = 0
        sub_mark = {}
        for i in range(len(stroka)):
            if stroka[i] in sub_mark and sub_mark[stroka[i]] >= start_index:
                start_index = sub_mark[stroka[i]] + 1
            sub_mark[stroka[i]] = i
            cnt_sub = i - start_index + 1
            max_sub = max(max_sub, cnt_sub)
        return max_sub


check = Solution()
print(check.lengthOfLongestSubstring("dvdf"))
