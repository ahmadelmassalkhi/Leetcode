# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # do nothing if length < 3
        if head == None or head.next == None or head.next.next == None:
            return

        # traverse until middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse right half
        right = slow.next
        right = self.reverseList(right)
        slow.next = None  # `slow` is tail of left list

        # get left half
        left = head
        while left and right:
            tempL = left.next
            tempR = right.next

            left.next = right
            right.next = tempL

            left = tempL
            right = tempR
