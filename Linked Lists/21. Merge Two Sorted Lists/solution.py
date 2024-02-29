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
            if list1.val < list2.val:
                if head == None:
                    head = list1
                else:
                    tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                if head == None:
                    head = list2
                else:
                    tail.next = list2
                tail = list2
                list2 = list2.next
        if list1 == None and list2 == None:
            return head
        if list1:
            if tail == None:
                return list1
            tail.next = list1
        if list2:
            if tail == None:
                return list2
            tail.next = list2
        return head
