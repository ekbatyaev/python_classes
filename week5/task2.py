"""
leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/word-break/description/
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


answer = Solution()
print(answer.wordBreak("leetcode", ["leet", "code"]))
print(answer.wordBreak("applepenapple", ["apple", "pen"]))
print(answer.wordBreak("cars", ["car", "ca", "rs"]))
print(answer.wordBreak("catskicatcats", ["cats", "cat", "dog", "ski"]))
