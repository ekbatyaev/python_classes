"""
leetcode.com/problem-list/hash-table/
url:https://leetcode.com/problems/replace-words/description
"""


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort()
        list_sentence = sentence.split(sep=" ")
        for i in range(len(list_sentence)):
            for word in dictionary:
                if list_sentence[i].startswith(word):
                    list_sentence[i] = word
                    break

        return " ".join(list_sentence)


answer = Solution()
print(
    answer.replaceWords(
        ["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery"
    )
)
print(answer.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
print(
    answer.replaceWords(
        ["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    )
)
