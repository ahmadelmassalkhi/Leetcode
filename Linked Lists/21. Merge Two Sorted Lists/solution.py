# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = tail = None
        while list1 and list2:
            minNode = list1 if list1.val < list2.val else list2
            if head == None:
                head = minNode
            else:
                tail.next = minNode
            tail = minNode
            if minNode == list1:
                list1 = list1.next
            else:
                list2 = list2.next
        if list1 == None and list2 == None:
            return head
        nonNullList = list1 if list1 else list2
        if tail == None:
            return nonNullList
        tail.next = nonNullList
        return head
