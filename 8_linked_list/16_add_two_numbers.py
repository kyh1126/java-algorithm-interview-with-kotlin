# Definition for singly-linked list.
from pip._vendor.typing_extensions import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution816:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        temp = answer

        while l1 or l2:
            if l1:
                sum = l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += temp.val

            temp.val = sum if sum < 10 else sum - 10
            temp.next = ListNode(1 if sum > 9 else 0)
            temp = temp.next

        temp.next = l1 or l2

        return answer


s = Solution816()
# [7,0,8]
l11 = ListNode(2, ListNode(4, ListNode(3, None)))
l12 = ListNode(5, ListNode(6, ListNode(4, None)))
print(s.addTwoNumbers(l11, l12).val)
# [0]
l21 = ListNode(0, None)
l22 = ListNode(0, None)
print(s.addTwoNumbers(l21, l22).val)
# [8,9,9,9,0,0,0,1]
l31 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
l32 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
print(s.addTwoNumbers(l31, l32).val)
