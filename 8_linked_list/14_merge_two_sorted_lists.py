# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution814:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        cur = answer

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 or list2

        return answer.next


s = Solution814()
# [1,1,2,3,4,4]
list11 = ListNode(1, ListNode(2, ListNode(4, None)))
list12 = ListNode(1, ListNode(3, ListNode(4, None)))
print(s.mergeTwoLists(list11, list12))
# []
list21 = None
list22 = None
print(s.mergeTwoLists(list21, list22))
# [0]
list31 = None
list32 = ListNode(0, None)
print(s.mergeTwoLists(list31, list32))
