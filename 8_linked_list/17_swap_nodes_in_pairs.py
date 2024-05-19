# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution817:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = head

        while answer and answer.next:
            curr_val = answer.val
            answer.val = answer.next.val
            answer.next.val = curr_val

            answer = answer.next.next

        return head


s = Solution817()
# [2,1,4,3]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(s.swapPairs(head1).val)
# []
head2 = None
print(s.swapPairs(head2))
# [1]
head3 = ListNode(1, None)
print(s.swapPairs(head3).val)
