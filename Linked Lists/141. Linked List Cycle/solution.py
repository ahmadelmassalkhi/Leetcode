# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        return False

    def hasCycle_set(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head:
            if head in s: return True
            s.add(head)
            head = head.next
        return False