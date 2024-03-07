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

    def getKth(self, head, k):
        if head == None or k <= 0: return None
        while head and k>0:
            head = head.next
            k -= 1
        return head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # skip unnecessary computations
        if k==1: return head
        
        dummy = prevGroup = ListNode(0, head)
        while True:
            kth = self.getKth(prevGroup, k)
            if kth == None:
                break # group not big enough (less than k)

            # store nextGroup's start
            temp = kth.next
            kth.next = None

            # reverse (and re-link)
            nextGroup = prevGroup.next
            prevGroup.next = self.reverse(prevGroup.next)
            nextGroup.next = temp

            # move
            prevGroup = nextGroup

        return dummy.next