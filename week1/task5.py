"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/edit-distance/description/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1) + 1
        m = len(word2) + 1
        count_dis = [0] * n
        for i in range(n):
            count_dis[i] = [0] * m

        for i in range(n):
            count_dis[i][0] = i

        for i in range(m):
            count_dis[0][i] = i

        for i in range(1, n):
            for j in range(1, m):
                if word1[i - 1] == word2[j - 1]:
                    count_dis[i][j] = count_dis[i - 1][j - 1]
                else:
                    count_dis[i][j] = min(
                        count_dis[i - 1][j] + 1,
                        count_dis[i][j - 1] + 1,
                        count_dis[i - 1][j - 1] + 1,
                    )
        return count_dis[n - 1][m - 1]


check = Solution()
print(check.minDistance("horse", "ros"))
print(check.minDistance("intention", "execution"))
