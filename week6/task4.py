"""
leetcode.com/problem-list/sliding-window/
url:https://leetcode.com/problems/swap-for-longest-repeated-character-substring/description
"""

from collections import Counter


class Solution:
    def maxRepOpt1(self, text: str) -> int:

        def check():
            return len(dict) != 2 or 1 not in dict.values()

        cnt = Counter(text)
        i, j, ans, dict = 0, 0, 0, {}
        for j, x in enumerate(text):
            dict[x] = dict.setdefault(x, 0) + 1
            while len(dict) != 1 and check():
                dict[text[i]] -= 1
                if dict[text[i]] == 0:
                    del dict[text[i]]
                i += 1
            if len(dict) == 1:
                (x,) = dict
                ans = max(ans, dict[x])
            else:
                x, y = dict
                if dict[y] == 1:
                    p = x
                else:
                    p = y
                if cnt[p] > dict[p]:
                    ans = max(ans, j - i + 1)
        return ans


# Пример использования:
answer = Solution()
print(answer.maxRepOpt1("ababa"))
print(answer.maxRepOpt1("aaabaaa"))
print(answer.maxRepOpt1("aaaaa"))
