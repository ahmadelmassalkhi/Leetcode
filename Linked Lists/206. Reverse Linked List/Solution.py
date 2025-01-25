# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = next = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    def reverseList_rec(self, head):
        if not head or not head.next: return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead