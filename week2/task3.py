"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        st_l = []
        path_answer = ""
        for i in range(len(path)):
            if path[i] == "" or path[i] == ".":
                continue
            elif path[i] == "..":
                if st_l:
                    st_l.pop(-1)
            else:
                st_l.append(path[i])
        path_answer = "/".join(st_l)
        return "/" + path_answer


answer = Solution()
print(answer.simplifyPath("/a//b////c/d//././/.."))
