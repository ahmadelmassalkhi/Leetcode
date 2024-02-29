# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def newNode(self, value):
        node = ListNode()
        node.val = value
        node.next = None
        return node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = None
        carryover = 0
        while l1 or l2 or carryover:
            # calculate new node's value
            sum = carryover
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # create new node
            node = self.newNode(sum % 10)
            carryover = sum / 10

            # append new node
            if head == None:
                head = node
            else:
                tail.next = node
            tail = node
        return head
