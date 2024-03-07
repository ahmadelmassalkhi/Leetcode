# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):

    def reverse(self, head):
        if head == None or head.next == None:
            return head
        newHead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newHead

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # skip unnecessary computations
        if k==1: return head
        
        # initialize
        i = 1
        start = dummy = ListNode(0,head)
        end = head
        while end and end.next:
            end = end.next
            i += 1
            if i == k:
                # store start of new k
                temp = end.next

                # reverse the list
                end.next = None # prevent reversing ALL list
                newHead = self.reverse(start.next)

                # re-link
                start.next.next = temp
                newStart = start.next
                start.next = newHead

                # prepare next k group reverse
                start = newStart
                end = start.next
                i = 1
        return dummy.next