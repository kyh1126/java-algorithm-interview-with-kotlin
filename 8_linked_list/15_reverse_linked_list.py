# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution815:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev = None

        while head:
            next = head.next
            head.next = rev
            rev = head
            head = next

        return rev


s = Solution815()
# [5,4,3,2,1]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(s.reverseList(head1))
# [2,1]
head2 = ListNode(1, ListNode(2, None))
print(s.reverseList(head2))
# []
head3 = None
print(s.reverseList(head3))
