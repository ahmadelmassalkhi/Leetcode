# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def check(self, head):
        if not head:
            return head
        if self.check(head.next) == False:
            return False
        if head.val != self.low.val:
            return False
        self.low = self.low.next
        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.low = head
        return self.check(head)
