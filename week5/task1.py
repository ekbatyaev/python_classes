"""
leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/group-anagrams/description/
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}
        for word in strs:
            s = sorted(word)
            hash_string = "".join(s)
            if words.get(hash_string) is None:
                words[hash_string] = [word]
            else:
                words[hash_string].append(word)
        return list(words.values())


answer = Solution()
print(answer.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
