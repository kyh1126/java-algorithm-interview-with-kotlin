from pip._vendor.typing_extensions import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution813:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next

        rev = None
        while slow:
            next = slow.next
            slow.next = rev
            rev = slow
            slow = next

        while rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next

        return True


s = Solution813()
# true
head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
print(s.isPalindrome(head1))
# false
head2 = ListNode(1, ListNode(2, None))
print(s.isPalindrome(head2))
