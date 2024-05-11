from pip._vendor.typing_extensions import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution813:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        target = head
        target_list = []

        while target:
            target_list.append(target.val)
            target = target.next

        target_list.reverse()

        for target_val in target_list:
            if head.val != target_val:
                return False
            else:
                head = head.next

        return True


s = Solution813()
# true
head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
print(s.isPalindrome(head1))
# false
head2 = ListNode(1, ListNode(2, None))
print(s.isPalindrome(head2))
