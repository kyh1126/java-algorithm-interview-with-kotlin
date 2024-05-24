# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution920:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        nextArr = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c not in dic:
                if len(nextArr) == 0 or c != nextArr.pop():
                    return False
            else:
                nextArr.append(dic[c])

        return len(nextArr) == 0


s = Solution920()
# True
s1 = "()"
print(s.isValid(s1))
# True
s2 = "()[]{}"
print(s.isValid(s2))
# False
s3 = "(]"
print(s.isValid(s3))
