import re


class Solution61:
    def isPalindrome(self, s: str) -> bool:
        target = "".join(re.findall("[\dA-Za-z]*", s.lower()))
        splitSeq = len(target) // 2

        if len(target) % 2 == 0:
            s2 = target[splitSeq:]
        else:
            s2 = target[splitSeq + 1:]

        return target[:splitSeq] == s2[::-1]


s = Solution61()
# true
print(s.isPalindrome("A man, a plan, a canal: Panama"))
# false
print(s.isPalindrome("race a car"))
# true
print(s.isPalindrome(" "))
