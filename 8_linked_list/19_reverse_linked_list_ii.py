# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution819:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode(0)
        root.next = head
        start = root
        count = 0
        rev = None

        while head:
            count += 1
            if count < left:
                start = start.next
                head = head.next
            elif left <= count <= right:
                next = head.next
                head.next = rev
                rev = head
                head = next
            else:
                break

        start.next = rev
        while start.next:
            start = start.next
        start.next = head

        return root.next


s = Solution819()
# [1,4,3,2,5]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
left1 = 2
right1 = 4
print(s.reverseBetween(head1, left1, right1).val)
# [5]
head2 = ListNode(5, None)
left2 = 1
right2 = 1
print(s.reverseBetween(head2, left2, right2).val)
