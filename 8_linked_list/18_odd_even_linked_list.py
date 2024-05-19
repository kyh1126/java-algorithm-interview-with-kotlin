# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution818:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next
        tail = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next

        odd.next = tail
        return head


s = Solution818()
# [1,3,5,2,4]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(s.oddEvenList(head1).val)
# [2,3,6,7,1,5,4]
head2 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7, None)))))))
print(s.oddEvenList(head2).val)
