"""
leetcode.com/problem-list/array/
url:https://leetcode.com/problems/merge-intervals/description/
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        changed_intervals = []
        intervals = sorted(intervals)
        changed_intervals.append(intervals[0])
        i = 0
        for interval in intervals:
            if changed_intervals[i][1] > interval[1]:
                continue
            elif changed_intervals[i][1] >= interval[0]:
                changed_intervals[i][1] = interval[1]
            else:
                changed_intervals.append(interval)
                i += 1

        return changed_intervals


answer = Solution()
print(answer.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(answer.merge([[1, 4], [4, 5]]))
print(answer.merge([[1, 4], [2, 3]]))
