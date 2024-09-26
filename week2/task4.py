"""
leetcode.com/problem-list/string/
url:https://leetcode.com/problems/restore-ip-addresses/description/
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        all_combinations = []

        def comb_ip(ip_adress, last_numbers):
            # print(ip_adress, last_numbers)
            if ip_adress.count(".") == 3 and last_numbers == "":
                all_combinations.append(ip_adress)
                return
            chislo_str = ""
            current = 0
            while current < len(last_numbers):
                if 0 < int(chislo_str + last_numbers[current]) <= 255:
                    chislo_str += last_numbers[current]
                    if len(ip_adress) != 0:
                        comb_ip(
                            ip_adress + "." + chislo_str, last_numbers[current + 1 :]
                        )
                    else:
                        comb_ip(chislo_str, last_numbers[current + 1 :])
                elif int(chislo_str + last_numbers[current]) == 0:
                    chislo_str += last_numbers[current]
                    if len(ip_adress) != 0:
                        comb_ip(
                            ip_adress + "." + chislo_str, last_numbers[current + 1 :]
                        )
                        break
                    else:
                        comb_ip(chislo_str, last_numbers[current + 1 :])
                        break
                else:
                    break

                current += 1

        comb_ip("", s)
        return all_combinations


answer = Solution()
print(answer.restoreIpAddresses("25525511135"))
print(answer.restoreIpAddresses("225948962"))
print(answer.restoreIpAddresses("101023"))
