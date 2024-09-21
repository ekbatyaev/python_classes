"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, stroka: str) -> str:
        message = []
        word = ""
        for i in range(len(stroka)):
            if stroka[i] != " " and i < len(stroka) - 1:
                word += stroka[i]
            elif stroka[i] == " " and len(word) != 0:
                message.append(word)
                word = ""
            elif stroka[i] != " " and i == len(stroka) - 1:
                word += stroka[i]
                message.append(word)
        answer = ""
        for i in range(len(message) - 1):
            answer += message[len(message) - i - 1] + " "
        answer += message[0]
        return answer


check = Solution()
print(check.reverseWords("hello world"))
print(check.reverseWords("the sky is blue"))
print(check.reverseWords("  hello world  "))
print(check.reverseWords("a good   example"))
