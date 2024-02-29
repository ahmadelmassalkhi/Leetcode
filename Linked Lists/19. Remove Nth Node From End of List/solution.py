# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def lengthOfList(self, head):
        if head == None:
            return 0
        return 1 + self.lengthOfList(head.next)

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.lengthOfList(head)
        if n == length:
            return head.next

        k = 1
        temp = head
        while k < length-n:
            temp = temp.next
            k += 1

        temp.next = temp.next.next
        return head
